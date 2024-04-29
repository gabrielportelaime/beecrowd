cw = 4.19
ci = 2.09
em = 335

def equilibrio_termico(massa_agua, massa_gelo, temp_agua, temp_gelo):
    energia_total = massa_agua * cw * (temp_agua - 0) + massa_gelo * ci * (0 - temp_gelo)
    gelo_derretido = min(massa_gelo, energia_total / (em + ci * temp_gelo))
    energia_total -= gelo_derretido * (em + ci * temp_gelo)
    temp_final = energia_total / (massa_agua + gelo_derretido) / cw
    return massa_agua + gelo_derretido, massa_gelo - gelo_derretido, temp_final


while(True):
    mw, mi, tw, ti = [int(x) for x in input().split()]
    agua, gelo, temp = equilibrio_termico(mw, mi, tw, ti)
    print(agua, gelo, temp)
    
