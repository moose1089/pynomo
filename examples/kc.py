"""
    kc.py

    Simple nomogram of type 2: F1 = F2 * F3

    Copyright (C) 2007-2009  Leif Roschier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys

sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer

N_params_1 = {
    'u_min': 0.0,
    'u_max': 100.0,
    'function': lambda u: u,
    'text_format': r"$%5.0f \%% $",
    'title': r'$edge$',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

N_params_2 = {
    'u_min': 0.01,
    'u_max': 1.0,
    'function': lambda u: 1*u,
    'title': r'$kelly$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
}

N_params_3 = {
    'u_min': 0.0,
    'u_max': 100.0,
    'text_format': r"$%5.0f \%% $",
    'function': lambda u: (100-u),
    'title': r'$ImpliedProbability$',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

block_1_params = {
    'block_type': 'type_2',
    'width': 10.0,
    'height': 10.0,
    'f1_params': N_params_1,
    'f2_params': N_params_2,
    'f3_params': N_params_3,
    'isopleth_values': [[27, 'x', 33]],
    #  V=60, P=33, e=27m k = 40
}

main_params = {
    'filename': 'kc.pdf',
    'paper_height': 14.0,
    'paper_width': 10.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.0), ('scale paper',)],
    'title_str': r'$kelly= {edge \over {1-ImpliedProbability}}$'
}
Nomographer(main_params)
