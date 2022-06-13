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
import math

sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer

N_params_1 = {
    'u_min': 0.0,
    'u_max': 100.0,
    'function': lambda u: u,
    'text_format': r"$%5.0f \%% $",
    'title': r'$edge$',
    'tick_levels': 3,
    'tick_side': 'left',
    'tick_text_levels': 2,
}

N_params_2 = {
    'u_min': 0.01,
    'u_max': 100.0,
    'function': lambda u: 1*u/100,
    'title': r'$Kelly\ proportion$',
    'tick_levels': 3,
    'tick_side': 'left',
    'tick_text_levels': 2,
    'text_format': r"$%5.0f \%% $",
    'scale_type': 'linear smart',
    'title_draw_center': True,
    'title_relative_offset': (0.7,0.2),
}

N_params_3 = {
    'title_draw_center': True,
    'title_relative_offset': (-1.0,1.5),
    'u_min': 0.0,
    'u_max': 100.0,
    'text_format': r"$%5.0f \%% $",
    'function': lambda u: (100-u),
    'title': r'$Implied\ Probability$',
    'tick_levels': 3,
    'tick_text_levels': 2
}

N_params_4 = {
    'u_min': 0.0,
    'u_max': 100.0,
    ## These for title top
   #  'title_x_shift': 2.5,
   # 'title_y_shift': -2.5,
    #These for title centre
    'title_relative_offset': (0.6,1.2),
    'text_format': r"$%5.0f \%% $",
    'function': lambda u: u/2.0,
    'title': r'$Model\ Probability$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_draw_center': True,
#     'title_extra_angle': 0
}

man1= {(i/100): (i/100) for i in range(100,110,1) }
man2= {(i/10): (i/10) for i in range(10,20,1) }
man3= {(i/10): (i/10) for i in range(20,30,1) }
man4= {(i/10): (i/10) for i in range(30,50,2) }
man5= {(i/10): (i/10) for i in range(50,85,5) }
man6= {(i/1): (i/1) for i in [1.15,9,10,12,15,20,30,50,100,1000] }
man={**man1,**man2,**man3,**man4,**man5,**man6}
man = { round(100/i,2): round(100/i,2) for i in range(2,102,2) }

N_params_5 = {
    'title_draw_center': True,
    'title_relative_offset': (+15.0,1.1),
    'u_min': 1,
    'u_max': 10000,
    #'scale_type': 'log smart',
    'text_format': r"$%5.2f$",
    'function': lambda u: 1000-1/(u),
    'title': r'$European Odds$',
    'tick_side': 'left',
    'tick_levels': 6,
    'tick_text_levels': 6,
    'scale_type': 'manual line',
    'manual_axis_data': man
}

block_1_params = {
    'block_type': 'type_2b',
    'width': 10.0,
    'height': 10.0,
    'f1_params': N_params_1, #edge
    'f2_params': N_params_2, #kc
    'f3_params': N_params_3, #IProb
    'f4_params': N_params_4, #Model
    'f5_params': N_params_5, #IP odds
    'isopleth_values': [[27, 'x', 33]],
    #  V=60, P=33, e=27m k = 40
}

main_params = {
    'filename': 'kc2.pdf',
    'paper_height': 27.0,
    'paper_width': 21.0,
    'block_params': [block_1_params],
    'title_y':25,
    'transformations': [('rotate', 0.0), ('scale paper',)],
    'extra_texts': [{
        'x': 5.1,
        'y': 24.5,
        'width': 15,
        'text': r'\LARGE $edge = {ModelProbability - ImpliedProbability}$ '},
        {
        'x': 5.1,
        'y': 23.5,
        'width': 15,
        'text': r'\LARGE $kelly= {edge \over {1-ImpliedProbability}}$'}],
    'title_str': '',
    'title_box_width': 15
}
Nomographer(main_params)
