import streamlit as st

st.set_page_config(
    page_title="EV Coil Parameter Estimator",
    page_icon=":car:",
    layout="centered",  
    initial_sidebar_state="auto",  
    
    
)

def calculate_values(Air_Gap, No_of_Turns, Metal_Shield):
    if Air_Gap >= 5 and Air_Gap <= 510:
        K = -8.544e-09 * Air_Gap ** 3 + 1.027e-05 * Air_Gap ** 2 - 0.004308 * Air_Gap + 0.6630
        K_round= round(K, 4)
        st.markdown("<h2 style='font-size: 26px;'>ESTIMATION COMPLETE</h2>", unsafe_allow_html=True)
        st.write("Here are the estimated values:")
       


        st.write("Coefficient of Magnetic Coupling:", K_round, '(dimensionsless)')
    else:
        K = float('nan')

    if No_of_Turns >= 5 and No_of_Turns <= 50:
        Mutual_Inductance = 0.07774 * No_of_Turns ** 2 + 2.497 * No_of_Turns - 16.51
        Mutual_Inductance_round = round(Mutual_Inductance,2)

        TX_L1 = 0.697 * No_of_Turns ** 2 + 2.745 * No_of_Turns - 18.16 - Metal_Shield ** 2 * 0.39112
        TX_L1_round = round(TX_L1,2)
        RX_L2 = 0.5677 * No_of_Turns ** 2 + 5.371 * No_of_Turns - 35.5 - Metal_Shield ** 2 * 0.39112
        RX_L2_round = round(RX_L2,2)
        L_avg = (TX_L1 + RX_L2) / 2
        L_avg_round = round(L_avg,2)

        st.write("\n TX Coil Inductance:", TX_L1_round,  'uH')
        st.write("RX Coil Inductance:", RX_L2_round,  'uH')
        st.write("Geometric Mean of Inductances", L_avg_round, 'uH')
        st.write("Mutual Inductance:", Mutual_Inductance_round, 'uH')

        R = (41.9 / 9.5) * No_of_Turns
        R_round = round(R,2)
        Q = (2 * 3.14159 * 85 * L_avg) / R
        Q_round = round(Q)
        Efficiency = (K * Q - 2) / (K * Q) * 100
        Efficiency_round = round(Efficiency,2)

        st.write("\n Q Factor:", Q_round, '(dimensionsless)')
        st.write("Efficiency (RF-RF)", Efficiency_round,'%')
        st.write("RDC:", R_round, 'mOhms')
        st.write("(These estimated results are based on simulated results obtained by S. Chatterjee under the mentorship and supervision of Prof. Polina Kapitanova)")
    else:
        Mutual_Inductance = float('nan')




def main():

    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.ibb.co/Fz12nN3/n2ni70f8k0q31.png");
    }
   </style>
    """,
    unsafe_allow_html=True
    
    st.markdown("<h2 style='font-size: 34px;'>EV Wireless Charging | Coil Parameter Estimator</h2>", unsafe_allow_html=True)
    st.write('Conforms to the SAE J2953_202010 Standard (https://www.sae.org/standards/content/j2954_202010/)')
    st.markdown("<h2 style='font-size: 16px;'>developed by S.Chatterjee | School of Physics and Engineering | ITMO University </h2>", unsafe_allow_html=True)
    st.write('https://physics.itmo.ru/en/personality/sutanu_chatterjee')
    st.write("This estimator utilises fitted curves of previously performed FEM simulation results and the application is programmed to solves quadratic and cubic polynomial functions in a real-time mode in order to estimate coil parameter values instantly, based on two major variables that are of much importance to WPT systems: Air Gap between the coils and Number of Turns of the individual coils.")


    st.markdown("<h2 style='font-size: 28px;'>PLEASE SELECT THE VALUES</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 18px;'>AIR GAP (mm)</h2>", unsafe_allow_html=True)
    #Air_Gap = st.number_input("Air Gap (mm):", min_value=10, max_value=510, value=160, step=1)
    Air_Gap = st.slider("Select a value for Air Gap in mm", min_value=10, max_value=510, value=160, step=1)
    st.markdown("<h2 style='font-size: 18px;'>NUMBER OF TURNS (no.)</h2>", unsafe_allow_html=True)
    #No_of_Turns = st.number_input("No. of Turns:", min_value=5, max_value=60, value=10, step=1)
    No_of_Turns = st.slider("Select a value for the Number of Turns ", min_value=5, max_value=60, value=10, step=1)
    st.markdown("<h2 style='font-size: 18px;'>ALU-METAL SHIELDING (mm)</h2>", unsafe_allow_html=True)
    Metal_Shield=st.slider("Select a value for the thickness of Aluminium Metal shield in mm", min_value=0, max_value=5, value=2, step=1)


    if st.button("ESTIMATE"):
        calculate_values(Air_Gap, No_of_Turns, Metal_Shield)

if __name__ == "__main__":
    main()
