
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
        st.markdown("<h2 style='font-size: 26px;color:green;'>ESTIMATION COMPLETE</h2>", unsafe_allow_html=True)
        st.write("Here are the estimated values:")
        st.write("Coefficient of Magnetic Coupling:", K_round, '(dimensionsless)')
    else:
        K = float('nan')

    if No_of_Turns >= 5 and No_of_Turns <= 50:
        Mutual_Inductance = 0.07774 * No_of_Turns ** 2 + 2.497 * No_of_Turns - 16.51
        Mutual_Inductance_round = round(Mutual_Inductance,2)

        TX_L1 = 0.697 * No_of_Turns ** 2 + 2.745 * No_of_Turns - 18.16 - Metal_Shield ** 2 * 0.49112
        TX_L1_round = round(TX_L1,2)
        RX_L2 = 0.5677 * No_of_Turns ** 2 + 5.371 * No_of_Turns - 35.5 - Metal_Shield ** 2 * 0.49112
        RX_L2_round = round(RX_L2,2)
        L_avg = (TX_L1 + RX_L2) / 2
        L_avg_round = round(L_avg,2)

        st.write("\n TX Coil Inductance:", TX_L1_round,  'uH')
        st.write("RX Coil Inductance:", RX_L2_round,  'uH')
        st.write("Geometric Mean of Inductances", L_avg_round, 'uH')
        st.write("Mutual Inductance:", Mutual_Inductance_round, 'uH')

        R = (45.9 / 9.5) * No_of_Turns**1.5
        R_round = round(R,2)
        Q = (2 * 3.14159 * 85 * L_avg) / R
        Q_round = round(Q)
        Efficiency = (K * Q - 2) / (K * Q) * 100
        Efficiency_round = round(Efficiency,2)

        st.write("\n Q Factor:", Q_round, '(dimensionsless)')
        st.write("Wireless Power Transmission Efficiency (RF-RF/AC-AC)", Efficiency_round,'%')
        st.write("DC Resistance:", R_round, 'mOhms')
        st.write("(These estimated results are based on simulated results obtained by S. Chatterjee under the mentorship and supervision of Prof. Polina Kapitanova)")
         st.markdown("<h2 style='font-size: 18px;color:green;'>THE STANDALONE VERSION OFFERS MORE FUNCTIONALITY CAN WE ARE ABLE TO MAKE A CUSTOM ONE BASED ON YOUR PARAMETERS. PLEASE CONTACT US.</h2>", unsafe_allow_html=True)
        st.image('interface.png')
    else:
        Mutual_Inductance = float('nan')

def main():
    st.image('header.png')
    #st.markdown("<h2 style='font-size: 34px;'>EV Wireless Charging | Coil Parameter Estimator</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 14px;'>developed by Sutanu Chatterjee and Polina Kapitanova | Department of Physics | ITMO University </h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 14px;color:orange;'>TERMS OF USE: This application provides estimated results, which may vary depending on several parameters that are not in control of the developers. We do not guarantee 100% accuracy and this application only provides estimated results based on the simulations that we performed.</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 18px;color:green;'>Conforms to the SAE J2953_202010 Standard</h2>", unsafe_allow_html=True)
    st.write("This estimator utilises fitted curves of previously performed FEM simulation results and the application is programmed to solves quadratic and cubic polynomial functions in a real-time mode in order to estimate coil parameter values instantly, based on two major variables that are of much importance to WPT systems: Air Gap between the coils and Number of Turns of the individual coils.")

    st.markdown("<h2 style='font-size: 28px;'>PLEASE SELECT THE VALUES</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 20px;'>AIR GAP (mm)</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 16px;'>Air Gap refers to the physical distance between two inductors and in a system of coupled coils, we consider it as the physical distance in air between the two coils, typically measured in millimeters. The coupling coefficient (k) of the system of coupled coils directly depends on this variable.</h2>", unsafe_allow_html=True)
    #Air_Gap = st.number_input("Air Gap (mm):", min_value=10, max_value=510, value=160, step=1)
    Air_Gap = st.slider("Select a value for Air Gap in mm", min_value=10, max_value=510, value=160, step=1)
    st.markdown("<h2 style='font-size: 20px;'>NUMBER OF TURNS (no.)</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 16px;'>Number of Turns refers to the winding number of an electrical conductor which is composed of an inductor or a coil. This is an adjustable variable and coil parameters such as Inductance, Resistance, Mutual Inductance, Q Factor etc. depend on it.</h2>", unsafe_allow_html=True)

    #No_of_Turns = st.number_input("No. of Turns:", min_value=5, max_value=60, value=10, step=1)
    No_of_Turns = st.slider("Select a value for the Number of Turns ", min_value=7, max_value=25, value=10, step=1)
    st.markdown("<h2 style='font-size: 20px;'>ALU-METAL SHIELDING (mm)</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 16px;'>Eddy currents are induced in aluminum plate during the transmission of energy from the TX coil in from of an alternating magnetic field. The partial energy is lost in the form of eddy current. However, eddy currents in the aluminum plate can also produce the corresponding inductive electromagnetic field which influences the original electromagnetic field, which leads to variations of coil parameters, leading to changes of WPT system working condition.</h2>", unsafe_allow_html=True)
    Metal_Shield=st.slider("Select a value for the thickness of Aluminium Metal shield in mm", min_value=0, max_value=5, value=0, step=1)

    

    if st.button("ESTIMATE"):
        calculate_values(Air_Gap, No_of_Turns, Metal_Shield)

if __name__ == "__main__":
    main()
