def poly_add2(list1, list2):
    result = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2]]
    return result


def poly_mult2(poly1, poly2):
    result = [(poly1[0] * poly2[0]),  # for first term (4th degree)
              (poly1[0] * poly2[1] + poly1[1] * poly2[0]),  # for second term (3rd degree)
              (poly1[0] * poly2[2] + poly1[1] * poly2[1] + poly1[2] * poly2[0]),  # for third term (2nd degree)
              (poly1[1] * poly2[2] + poly1[2] * poly2[1]),  # for fourth term (1st degree)
              (poly1[2] * poly2[2])]  # for fifth term (0 degree)
    return result
