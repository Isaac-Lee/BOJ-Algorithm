t1, m1, t2, m2 = map(int, input().split())
m_1 = t1*60+m1
m_2 = t2*60+m2
if m_2 < m_1:
    m_2 += 24*60
m = m_2-m_1
print(m, m//30)
