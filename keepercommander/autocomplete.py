#  _  __
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|
#
# Keeper Commander
# Copyright 2018 Keeper Security Inc.
# Contact: ops@keepersecurity.com
#

import argparse
import itertools
import shlex

from prompt_toolkit.completion import Completion, Completer

from .params import KeeperParams
from .commands.folder import mv_parser
from .commands import commands, enterprise_commands
from . import api
from .subfolder import try_resolve_path as sf_try_resolve_path


def no_parse_exception(m):
    pass


def no_exit():
    pass


record_parser = argparse.ArgumentParser()
record_parser.add_argument('-e', '--email', dest='email', action='append')
record_parser.add_argument('-a', '--action', dest='action', action='store')
record_parser.add_argument('--notes', dest='notes', action='store')
record_parser.add_argument('record', nargs='?', type=str, action='store', help='record path or UID')
record_parser.error = no_parse_exception
record_parser.exit = no_exit

folder_parser = argparse.ArgumentParser()
folder_parser.add_argument('-e', '--email', dest='email', action='append')
folder_parser.add_argument('-a', '--action', dest='action', action='store')
folder_parser.add_argument('-r', '--record', dest='record', action='append')
folder_parser.add_argument('folder', nargs='?', type=str, action='store', help='record path or UID')
folder_parser.error = no_parse_exception
folder_parser.exit = no_exit


def unescape_string(have_initial_double_quote, string):
    """Remove escape sequences; return a literal string for matching."""
    if have_initial_double_quote:
        tuple_ = (
            ('//', '/'),
            ('\\"', '"'),
            ('\\\\', '\\'),
        )
    else:
        tuple_ = (
            ('//', '\0'),
            ('\\ ', ' '),
            ('\\"', '"'),
            (r"\'", "'"),
            ('\\\\', '\\'),
            ('\0', '/'),
        )
    for from_str, to_str in tuple_:
        string = string.replace(from_str, to_str)
    return string



def escape_string(have_initial_double_quote, string):
    """Replace special characters in string, for interactive shell quoting, as part of tab-completion."""
    if have_initial_double_quote:
        tuple_ = (
            ('\\', '\\\\'),
            ('"', r'\"'),
            ('/', '//'),
        )
    else:
        tuple_ = (
            ('\\', '\\\\'),
            ("'", r"\'"),
            (' ', r'\ '),
            ('"', r'\"'),
            ('/', '//'),
        )
    for from_str, to_str in tuple_:
        string = string.replace(from_str, to_str)
    return string


class CommandCompleter(Completer):
    def __init__(self, params, aliases):
        # type: (CommandCompleter, KeeperParams, dict) -> None
        Completer.__init__(self)
        self.params = params
        self.commands = commands
        self.aliases = aliases

    @staticmethod
    def fix_input(txt):
        is_escape = False
        is_quote = False
        is_double_quote = False
        for c in txt:
            if c == '\\':
                is_escape = not is_escape
            elif not is_escape:
                if c == '\'':
                    if is_double_quote:
                        return None
                    is_quote = not is_quote
                elif c == '"':
                    if is_quote:
                        return None
                    is_double_quote = not is_double_quote

        if is_quote:
            txt = txt + '\''

        if is_double_quote:
            txt = txt + '"'

        return txt

    def get_completions(self, document, complete_event):
        try:
            if document.is_cursor_at_the_end:
                pos = document.text.find(' ')
                if pos == -1:
                    cmds = [x for x in commands if x.startswith(document.text)]
                    if self.aliases:
                        al_cmds = [x[0] for x in self.aliases.items() if type(x[1]) == tuple and x[0].startswith(document.text)]
                        cmds.extend(al_cmds)
                    if self.params.enterprise:
                        e_cmds = [x for x in enterprise_commands if x.startswith(document.text)]
                        cmds.extend(e_cmds)
                    if len(cmds) > 0:
                        cmds.sort()
                        for c in cmds:
                            yield Completion(c, start_position=-len(document.text))
                elif pos > 0:
                    cmd = document.text[:pos]
                    if cmd in self.aliases:
                        ali = self.aliases[cmd]
                        if type(ali) == tuple:
                            cmd = ali[0]
                        else:
                            cmd = ali
                    extra = dict()
                    raw_input = document.text[pos+1:].lstrip()
                    extra['have_initial_double_quote'] = bool(raw_input) and raw_input[0] == '"'
                    context = ''
                    if cmd in {'download-attachment', 'upload-attachment', 'share-record', 'edit', 'append-notes',
                               'rm', 'ls', 'clipboard-copy', 'find-password'}:
                        args = CommandCompleter.fix_input(raw_input)
                        if args is not None:
                            opts, _ = record_parser.parse_known_args(shlex.split(args))
                            extra['prefix'] = opts.record or ''
                            context = 'path'
                    elif cmd in {'share-folder', 'mkdir', 'tree', 'rmdir', 'cd', 'record-permission'}:
                        args = CommandCompleter.fix_input(raw_input)
                        if args is not None:
                            opts, _ = folder_parser.parse_known_args(shlex.split(args))
                            extra['prefix'] = opts.folder or ''
                            context = 'folder'
                    elif cmd in {'mv', 'ln'}:
                        args = CommandCompleter.fix_input(raw_input)
                        if args is not None:
                            opts, _ = mv_parser.parse_known_args(shlex.split(args))
                            if opts.dst is None:
                                word = document.get_word_under_cursor()
                                if len(word) == 0 and len(opts.src or '') > 0:
                                    extra['prefix'] = ''
                                    context = 'folder'
                                else:
                                    extra['prefix'] = opts.src or ''
                                    context = 'path'
                            else:
                                extra['prefix'] = opts.dst or ''
                                context = 'folder'
                    elif cmd == 'help':
                        args = CommandCompleter.fix_input(raw_input)
                        if args is not None:
                            extra['prefix'] = args
                            context = 'command'
                    elif cmd == 'connect':
                        args = CommandCompleter.fix_input(raw_input)
                        if args is not None:
                            extra['prefix'] = args
                            context = 'connect'

                    if context in {'folder', 'path'}:
                        rs = sf_try_resolve_path(self.params, extra['prefix'])
                        if rs is not None:
                            folder, possible_prefix = rs
                            is_path = False if possible_prefix else True
                            unescaped_possible_prefix = unescape_string(extra['have_initial_double_quote'], possible_prefix)
                            for uid in folder.subfolders:
                                f = self.params.folder_cache[uid]
                                full_folder_or_path_str = f.name
                                if (
                                    full_folder_or_path_str.startswith(unescaped_possible_prefix) and 
                                    len(unescaped_possible_prefix) < len(full_folder_or_path_str)
                                ):
                                    escd_full_folder_or_path_str = escape_string(
                                        extra['have_initial_double_quote'],
                                        full_folder_or_path_str,
                                    )
                                    if is_path and not extra['prefix'].endswith('/') and bool(extra['prefix']):
                                        escd_full_folder_or_path_str = '/' + escd_full_folder_or_path_str
                                    # This is a little precarious.  shlex has stripped out the quoting previously, and we've
                                    # imposed our own layer of quoting as well.  Here we're trying to put it back the way it
                                    # was for just /part/ of the original input.  If we don't get it precisely correct,
                                    # then the completion will appear in the wrong place in the line of edited text in the
                                    # keeper shell.
                                    escaped_possible_prefix = escape_string(
                                         extra['have_initial_double_quote'],
                                         unescaped_possible_prefix,
                                    )
                                    yield Completion(
                                        text=escd_full_folder_or_path_str,
                                        display=escd_full_folder_or_path_str + '/',
                                        start_position=-len(escaped_possible_prefix),
                                    )

                            if context == 'path':
                                possible_prefix = possible_prefix.lower()
                                folder_uid = folder.uid or ''
                                if folder_uid in self.params.subfolder_record_cache:
                                    for uid in self.params.subfolder_record_cache[folder_uid]:
                                        r = self.params.record_cache[uid]
                                        if 'display_name' not in r:
                                            rec = api.get_record(self.params, uid)
                                            r['display_name'] = rec.title or rec.record_uid
                                        n = r.get('display_name') or ''
                                        if len(n) > 0:
                                            if n.lower().startswith(possible_prefix) and len(possible_prefix) < len(n):
                                                n = escape_string(extra['have_initial_double_quote'], n)
                                                d = n
                                                if len(d) > 39:
                                                    d = d[:29] + '...' + d[-7:]
                                                yield Completion(text=n, display=d, start_position=-len(possible_prefix))
                    elif context == 'command':
                        cmd = extra['prefix']
                        for c in itertools.chain(commands.keys(), enterprise_commands.keys()):
                            if c.startswith(cmd):
                                yield Completion(c, display=c, start_position=-len(cmd))

        except Exception as e:
            pass

