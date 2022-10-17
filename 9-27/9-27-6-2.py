def square_root():
    i = 0
    c = 2
    m_max = c
    m_min = 0
    g = (m_min + m_max)/2
    while (abs(g*g - c)>0.00000000001):
        if (g*g < c):
            m_min = g
        else:
            m_max = g
        g = (m_min + m_max) / 2
        i = i + 1
        print('%d:g = %.13f' % (i,g))

square_root()