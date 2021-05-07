from sympy.solvers import solve
from sympy import Symbol, symbols,Eq
ma,va,mb,vb,vap,vbp,e,h,u,x=symbols('ma va mb vb vap vbp e h u x')

#ecuaciones momento
eqn1=Eq(ma*va+mb*vb,ma*vap+mb*vbp)
eqn2=Eq((va-vb)*e,vbp-vap)
#ecuaciones de conservacion de energia
eqn3=Eq(1/2*ma*vap**2,ma*9.81*h)
eqn4=1/2*mb*vbp**2-u*mb*9.81*x


#Variables
e_v=0.8
ma_v=0.5
va_v=0
mb_v=1
vb_v=2
u_v=0.6

#Funcion helper de asignacion de Variables
def set_vars(e_va,ma_va,va_va,mb_va,vb_va,u_va):
    global e_v,ma_v,va_v,mb_v,vb_v,u_v
    e_v=e_va
    ma_v=ma_va
    va_v=va_va
    mb_v=mb_va
    vb_v=vb_va
    u_v=u_va

def resolver():
    res=solve((eqn1,eqn2),vbp,vap)
    res1=solve(eqn3,h)
    res2=solve(eqn4,x)
    v_a_p=res[vap]
    v_b_p=res[vbp]
    v_a_p=v_a_p.subs([(e,e_v),(ma,ma_v),(va,va_v),(mb,mb_v),(vb,vb_v)])
    v_b_p=v_b_p.subs([(e,e_v),(ma,ma_v),(va,va_v),(mb,mb_v),(vb,vb_v)])
    h_v=res1[0].subs([(ma,ma_v),(vap,v_a_p)])
    x_v=res2[0].subs([(mb,mb_v),(u,u_v),(vbp,v_b_p)])
    #print("h={} x={}".format(h_v,x_v))
    return h_v,x_v

if __name__ == '__main__':
    for i in range(11):
        set_vars(0.8,0.5,0,1,2+(i/10),0.6)
        h_v,x_v=resolver()
        print("Para vb={} h={} y x={}".format(2+(i/10),h_v,x_v))
    #
    #print(x_v)
    # set_vars(0.8,0.5,0,1,2,0.6)
    # h_v,x_v=resolver()
    # print("Para e={} h={} y x={}".format(x,h_v,x_v))
