import streamlit as st
import pandas as pd
import joblib
import warnings 
warnings.filterwarnings('ignore')

data = pd.read_csv('Financial_inclusion_dataset.csv')

st.markdown("<h1 style = 'color: #0E46A3; text-align: center; font-size: 60px; font-family: Georgia'>BANK EASE</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #0E46A3; text-align: center; font-family: italic'>Built By Faith</h4>", unsafe_allow_html = True)

st.markdown("<br>", unsafe_allow_html=True)

# #add image
st.image('pngwing.com (20).png', width = 800, caption ='Built by Faith')

st.markdown("<h2 style = 'color: #0E46A3; text-align: center; font-family: montserrat '>BACKGROUND OF STUDY</h2>", unsafe_allow_html = True)

st.markdown("<p>The objective of this model is to develop a predictive model capable of accurately assessing the eligibility of potential customers based on their demographic information, financial history, and other relevant factors. By leveraging machine learning techniques, the goal is to create a system that can automate the eligibility determination process, thereby streamlining and improving the efficiency of customer onboarding for the bank. Ultimately, the aim is to enhance customer experience, reduce operational costs, and ensure compliance with regulatory requirements such as KYC (Know Your Customer) and AML (Anti-Money Laundering)..</p>", unsafe_allow_html = True)

st.sidebar.image('pngwing.com (19).png', caption = 'Welcome Faith')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.header('Project Data')
st.dataframe(data, use_container_width = True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)


st.sidebar.subheader('User Input Variables')

sel_cols = ['age_of_respondent', 'household_size', 'job_type', 'education_level', 'marital_status', 'country',
            'location_type', 'relationship_with_head', 'bank_account']

age = st.sidebar.number_input('age', data['age_of_respondent'].min(), data['age_of_respondent'].max())
household = st.sidebar.number_input('household_size', data['household_size'].min(), data['household_size'].max())
job = st.sidebar.selectbox('job_type', data['job_type'].unique())
education = st.sidebar.selectbox('education_level', data['education_level'].unique())
marital = st.sidebar.selectbox('marital_status', data['marital_status'].unique())
country = st.sidebar.selectbox('country', data['country'].unique())
location = st.sidebar.selectbox('location_type', data['location_type'].unique())
rel_head = st.sidebar.selectbox('relationship_with_head', data['relationship_with_head'].unique())
# bank_acc= st.sidebar.selectbox('bank_account', data['bank_account'].unique())



#users input
input_var = pd.DataFrame()
input_var['age_of_respondent'] = [age]
input_var['household_size'] = [household]
input_var['job_type'] = [job]
input_var['education_level'] = [education]
input_var['marital_status'] = [marital]
input_var['country'] = [country]
input_var['location_type'] = [location]
input_var['relationship_with_head'] = [rel_head]
#input_var['bank_account'] = [bank_acc]



st.markdown("<br>", unsafe_allow_html= True)
st.divider()
st.subheader('Users Inputs')
st.dataframe(input_var, use_container_width = True)

# import the transformers
job_type = joblib.load('job_type_encoder.pkl')
education_level = joblib.load('education_level_encoder.pkl')
marital_status = joblib.load('marital_status_encoder.pkl')
country = joblib.load('country_encoder.pkl')
location_type = joblib.load('location_type_encoder.pkl')
relationship_with_head = joblib.load('relationship_with_head_encoder.pkl')
bank_account = joblib.load('bank_account_encoder.pkl')



# transform the users input with the imported encoders
input_var['job_type'] = job_type.transform(input_var[['job_type']])
input_var['education_level'] = education_level.transform(input_var[['education_level']])
input_var['marital_status'] = marital_status.transform(input_var[['marital_status']])
input_var['country'] = country.transform(input_var[['country']])
input_var['location_type'] = location_type.transform(input_var[['location_type']])
input_var['relationship_with_head'] = relationship_with_head.transform(input_var[['relationship_with_head']])
#input_var['bank_account'] = bank_account.transform(input_var[['bank_account']])



# st.header('Transformed Input Variable')
# st.dataframe(input_var, use_container_width = True)

# st.dataframe(input_var)
model = joblib.load('MideFinanceModel.pkl')
predict = model.predict(input_var)

if st.button('Confirm Your Eligibility'):
    if predict[0] == 0:
        st.error(f"Unfortunately...You are not eligible to open or have a bank account")
        st.image('denied.png', width = 300)
    else:
        st.success(f"Congratulations... You are eligible to open and have a bank account. Please proceed to any of our offices to open an account")
        st.image('approved 2.png', width = 300)
        st.balloons()


#Primary color - #FF4B4B
#Background color - #FFFFFF
#Text color - # 31333F
#Secondary color - #F0F2F6
#Font Family - Sans serif


 



