import pickle
import joblib,os
import streamlit as st


def load_prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

def main():
    st.title("Currency Value Prediction")
    st.write("---")
    st.header('Enter Currecy Valule')
    col1, col2, col3 = st.columns(3)
    with col1:
        cny = st.number_input("CNY", help="China")
    with col2:
        pak = st.number_input("PKL", help="Pakisthan")
    with col3:
        lkr = st.number_input("LKR", help="Sri Lanka")
    col4, col5, col6 = st.columns(3)
    with col4:
        amd = st.number_input("AMD", help="Armenia")
    with col5:
        btd = st.number_input("BTD", help="Bangladesh")
    with col6:
        btn = st.number_input('BTN', help="Butan")
    col7, col8, col9 = st.columns(3)
    with col7:
        cve = st.number_input("CVE", help="REPUBLIC OF CAPE VENDER") 
    with col8:
        xof = st.number_input('XOF', help="WEST-AFRICA NATIONS")
        alb = st.number_input('ALL', help="Albania")
    with col9:
        aoa = st.number_input('AOA', help="Angola")
    
    predict = st.button("Predict")
    if predict:
        model = pickle.load(open('CRPRED.pkl', 'rb'))
        pred_currency = model.predict([[cny, pak, lkr, amd, btd, btn, cve, xof, aoa, alb]])
        st.header('The Estimated Currecy value is ₹ {}'.format(round(pred_currency[0],2)))
    
if __name__=='__main__':
    main()