def diff_time(h1,m1,h2,m2):
    first_total_min = h1*60 + m1
    sec_total_min = h2*60 + m2

    final_time = sec_total_min - first_total_min

    print(f'{final_time//60}:{final_time%60}')

diff_time(15,23,18,54)