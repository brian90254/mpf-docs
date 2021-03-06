import ast
import os
import re

paths = ['../../mpf/mpf', '../../mpf-mc/mpfmc']
rst_path = '../events'


class EventDocParser(object):

    def __init__(self):
        self.file = None
        self.file_list = list()

    def parse_file(self, file_name):

        self.file = file_name

        with open(file_name) as f:
            my_ast = ast.parse(f.read())

        for x in ast.walk(my_ast):
            if isinstance(x, ast.Str) and (x.s.strip().lower().startswith(
                    'event:')):
                event, rst = self.parse_string(x)

                if rst:
                    filename = self.create_file(event, rst)
                    self.file_list.append((event, filename))

    def write_index(self):

        index = '''Event reference
===============

Here's a list of all the "built in" events that are included in MPF and the
MPF MC. Of course your own machine could include custom events that aren't
on the list here.

See the :doc:`Event Manager overview </core/events>` for more information on
how MPF uses events.

.. toctree ::
   :maxdepth: 1

'''

        self.file_list.sort()

        for file_name in self.file_list:
            index += '   {} <{}>\n'.format(file_name[0], file_name[1][:-4])

        with open(os.path.join(rst_path, 'index.rst'), 'w') as f:
            f.write(index)

    def create_file(self, event, rst):
        filename = event.replace('(', '').replace(')', '') + '.rst'

        with open(os.path.join(rst_path, filename), 'w') as f:
            f.write(rst)

        return filename

    def parse_string(self, string):
        # string = string.s.replace('\n', ' ')  # strip newlines
        # string = ' '.join(string.s.split(' '))  # strip extra spaces
        string = '\n'.join(' '.join(line.split())
                           for line in string.s.split('\n'))

        string = string.replace('Event:', 'event:')
        string = string.replace('Desc:', 'desc:')

        try:
            string = string.replace('Args:', 'args:')
        except ValueError:
            pass

        final_dict = self.string_to_args_dict(string, ['event', 'desc',
                                                       'args'])

        if 'desc' not in final_dict:
            # not an events docstring
            return (None, None)

        return self.build_rst_entry(final_dict)

    def string_to_args_dict(self, string, args):
        index_starts = list()

        for arg in args:
            try:
                index_starts.append(string.index(arg + ':'))
            except ValueError:
                pass

        index_starts.sort()
        sliced_list = list()
        for x in range(len(index_starts)):
            try:
                sliced_list.append(string[index_starts[x]:index_starts[
                    x + 1]])
            except IndexError:
                sliced_list.append(string[index_starts[x]:])

        final_dict = dict()

        for entry in sliced_list:
            split_entry = entry.split(':', 1)
            final_dict[split_entry[0].strip()] = split_entry[1].strip()

        return final_dict

    def build_rst_entry(self, final_dict):
        rst_output = str()

        # write the title
        try:
            rst_output += final_dict['event']+ '\n'
        except KeyError:
            print("Events entry missing from: {}".format(self.file))

        rst_output += ('=' * len(final_dict['event'])) + '\n\n'
        rst_output += '*MPF Event*\n\n'

        # add the description
        rst_output += final_dict['desc'] + '\n\n\n'

        # add the keyword arguments section

        rst_output += 'Keyword arguments\n'
        rst_output += '-----------------\n\n'

        if 'args' in final_dict:
            rst_output += self.parse_args(final_dict['args'])
        else:
            rst_output += '*None*\n'

        return final_dict['event'], rst_output

    def parse_args(self, args_string):

        args = list()
        output = str()

        for x in re.findall('\\b(\w*)\\b(?=\:)', args_string):
            if x:
                args.append(x)

        args_dict = self.string_to_args_dict(args_string, args)

        for k, v in sorted(args_dict.items()):
            output += k + '\n'
            output += ('~' * len(k)) + '\n'
            output += v + '\n\n'

        return output

if __name__ == '__main__':
    a = EventDocParser()

    # delete existing files
    for path, _, files in os.walk(rst_path):
        for file in files:
            if file != 'index.rst':
                os.remove(os.path.join(path, file))

    # walk through the folders to scan
    for path in paths:
        for root, _, files in os.walk(path):
            for file in [x for x in files if x.endswith('.py')]:
                a.parse_file(os.path.join(root, file))

    # create the index.rst based on everything that was found
    a.write_index()
