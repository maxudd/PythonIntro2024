import re

number = input()

x_pattern = r'(%0x[0-9a-f]{1,16})'
o_pattern = r'(%0o[0-7]{1,8})'
b_pattern = r'(%0b[01]{1,20})'

norm_pattern_non_d = fr'({x_pattern}|{o_pattern}|{b_pattern})'
norm_pattern_d = r'(\d+)'
norm_pattern = fr'({norm_pattern_non_d}|{norm_pattern_d})'

frac_pattern = fr'(\.({norm_pattern_d}|(0*{norm_pattern_non_d})))'
exp_pattern = fr'(-?{norm_pattern}{frac_pattern}?E([\+-]{norm_pattern})?)'

num_pattern = re.compile(fr'^({exp_pattern}|(-?{norm_pattern}))$')

res = num_pattern.match(number)

if res:
    print('YES')
else:
    print('NO')