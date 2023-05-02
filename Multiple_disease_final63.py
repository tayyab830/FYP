# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st

from streamlit_option_menu import option_menu







#loaded_model = pickle.load(open('C:/Users/home/Desktop/FyP Finals/Models/Schizophrenia with log/Schizophrenia.sav', 'rb'))
#loaded_model = pickle.load(open('C:/Users/home/Desktop/FyP Finals/Models/Alchoho with log/alcohol_addiction.sav', 'rb'))




def Behavioral_addiction_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    behavioral_model = pickle.load(open('behavioral_addiction.sav', 'rb'))


        
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = behavioral_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Behavioral Addiction .'
    else:
      return'You do not have any indications of Behavioral Addiction .'




def Trauma_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    Trauma_loaded_model = pickle.load(open('trauma.sav', 'rb'))


        
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = Trauma_loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Trauma and stress related disorder .'
    else:
      return'You do not have any indications of Trauma and stress related disorder .'




def Depression_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    dep_Depression_Prediction = pickle.load(open('depression.sav', 'rb'))


        
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = dep_Depression_Prediction.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Depression .'
    else:
      return'You do not have any indications of Depression .'
    



def Anxiety_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    loaded_model = pickle.load(open('Anxiety.sav', 'rb'))


        
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Anxiety .'
    else:
      return'You do not have any indications of Anxiety .'



def Schizophrenia_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    loaded_model = pickle.load(open('Schizophrenia.sav', 'rb'))

        
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Schizophrenia .'
    else:
      return'You do not have any indications of Schizophrenia .'





def Alchohol_Prediction(input_data):

    # changing the input_data to numpy array
    string_list = np.asarray(input_data)
    al_loaded_model = pickle.load(open('alcohol_addiction.sav', 'rb'))
    
    input_data_as_numpy_array = [float(x) for x in string_list]
    print(input_data_as_numpy_array)

    log_arr = np.log(input_data_as_numpy_array)
    input_data_as_numpy_array=log_arr
    print(input_data_as_numpy_array)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    print(input_data_as_numpy_array)

    prediction = al_loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'There is an inidcation the you might have Alchohol .'
    else:
      return'You do not have any indications of Alchohol .'




#--------------------------------------------------------------------

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu(menu_title=None,
                          
                          options=['Home','Anxiety Disorder',
                           'Depressive Disorder',
                           'Alcohol addiction',
                           'Behavioral Addiction',
                           'Trauma & Stress related Disorder',
                           'Schizophrenia','About'],
                          menu_icon='house',
                          icons=['house','emoji-angry','emoji-frown','emoji-wink','emoji-expressionless','emoji-dizzy','emoji-neutral','file-earmark-person-fill'],
                          default_index=0)

if selected == 'Home':
    st.header("Brain Bolt")
    st.subheader("EEG based Mind Aid")
    st.markdown(">Objective : ")
    st.write("Our project aimed to develop an accessible and efficient machine learning-based approach to screen for common mental health disorders using EEG data, overcoming the challenges of traditional methods of diagnosis and assessment.")
    st.markdown("---")
    st.markdown(">Conclusion : ")
    st.write("In summary, our project focused on utilizing rest state QEEG data to detect common mental health disorders, such as schizophrenia, alcohol use disorder, anxiety disorders, depressive disorder, trauma and stress-related disorders, behavioral addiction, internet addiction, and gambling addiction. By using SVM, we achieved an accuracy of over 70% with good precision, recall, and f1 values. We also included a self-assessment option based on DSM 5 diagnostic criteria, allowing users to assess their mental health by answering 10 simple questions for each disease.")

    st.write("To improve the accuracy of our model, we utilized top features for binary classification for each disease with healthy control data. Our findings highlight the potential of using EEG-based analysis for mental health screening and diagnosis. However, future research and development are needed to increase the sample size and balance the data for further accuracy improvement.")
    st.write("Our GUI application built with Streamlit allows users to easily access the self-assessment feature and obtain assessments based on simple questions based on dsm-5 criteria and prediction scores for each disease by entering the QEEG values. Our project showcases the potential of pre-processed QEEG data for disease prediction using various ML algorithms, with SVM being a preferred model due to its ability to avoid overfitting. Overall, our proposed solution provides an effective and accessible method for mental health screening and diagnosis.")
    st.markdown("---")

elif selected == 'About':
    import streamlit as st
    
    # Add project title
    st.title('Project: Brain Bolt - EEG based Mind Aid')
    st.markdown("---")
    # Add group members
    st.subheader('Group Members')
    st.write('MUDASSIR HUSSAIN SAQIB')
    st.write('IMAMA RAJA')
    st.write('ADEEBA ZAHRA')
    st.write('MUHAMMAD TAYYAB GULZAR')
    st.markdown("---")
    # Add supervisor and co-supervisor
    st.subheader('Supervisor')
    st.write('Imran Javaid')
    st.write ('EE Dept MCS')
    st.subheader('Co-supervisor')
    st.write('Dr. Shemaila Saleem')
    st.write('(Physiology dept, FMDC)')

    

    


elif selected == 'Anxiety Disorder':
    
    #sd
    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:
        import streamlit as st

        # Page title
        st.title('Anxiety Disorder')
        
        # Introduction
        st.header('Introduction')
        st.write('Anxiety disorder is a mental health condition that causes excessive and persistent worry, fear, and nervousness. It can interfere with daily activities and may lead to physical symptoms such as sweating, trembling, and rapid heartbeat. Anxiety disorder is one of the most common mental health disorders, affecting millions of people worldwide.')
        
        # Symptoms
        st.header('Symptoms')
        st.write('Anxiety disorder can present a variety of symptoms, including:')
        st.write('- Excessive worry and fear')
        st.write('- Feeling restless or on edge')
        st.write('- Irritability')
        st.write('- Difficulty concentrating')
        st.write('- Muscle tension')
        st.write('- Sleep disturbances')
        st.write('- Panic attacks')
        
        # Causes
        st.header('Causes')
        st.write('The causes of anxiety disorder are not fully understood, but may include a combination of genetic, environmental, and lifestyle factors. Some risk factors for anxiety disorder include:')
        st.write('- Family history of anxiety disorder')
        st.write('- Trauma or stressful life events')
        st.write('- Chronic medical conditions')
        st.write('- Substance abuse')
        
        # Treatment
        st.header('Treatment')
        st.write('Treatment for anxiety disorder may include therapy, medication, or a combination of both. Cognitive behavioral therapy (CBT) is a common type of therapy used to treat anxiety disorder. Medications such as antidepressants and anti-anxiety medications may also be prescribed. Lifestyle changes such as regular exercise, healthy eating, and stress reduction techniques may also be helpful.')
        
        # Conclusion
        st.header('Conclusion')
        st.write('Anxiety disorder can be a challenging condition to live with, but effective treatments are available. It is important to seek help if you are experiencing symptoms of anxiety disorder.')
        
                
    
 
    
 
    with tabs[1]:
    
        # page title
        st.title('Anxiety Disorder')
        st.markdown('> Enter the PSD and FC values for Anxiety prediction .')
        st.markdown('---')
    
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        with col1:    
            COH_alpha_F8_T4 = st.text_input('COH.alpha.F8.T4')
            COH_alpha_P4_O2 = st.text_input('COH.alpha.P4.O2')
            COH_beta_F4_O2 = st.text_input('COH.beta.F4.O2')
            COH_beta_F8_O2 = st.text_input('COH.beta.F8.O2')
            COH_delta_T5_P3 = st.text_input('COH.delta.T5.P3')
        with col2:
            COH_gamma_T5_P3 = st.text_input('COH.gamma.T5.P3')
            COH_theta_T5_P3 = st.text_input('COH.theta.T5.P3')
            delta_O1 = st.text_input('delta.O1')
            delta_O2 = st.text_input('delta.O2')
            delta_T5 = st.text_input('delta.T5')
        with col3:
            beta_FP2 = st.text_input('beta.FP2')
            gamma_F8 = st.text_input('gamma.F8')
            gamma_T4 = st.text_input('gamma.T4')
            theta_C3 = st.text_input('theta.C3')
            theta_Cz = st.text_input('theta.Cz')
    
        st.markdown('---')
                
        #code for prediction
        
       
        
        # creating a button for prediction
        
        if st.button('Anxiety Test Result '):
            diagnosis_anx = Anxiety_Prediction([delta_O2, gamma_T4, COH_beta_F8_O2, delta_T5, COH_alpha_F8_T4, COH_beta_F4_O2, COH_delta_T5_P3, gamma_F8, COH_alpha_P4_O2, beta_FP2, theta_C3, delta_O1, theta_Cz, COH_theta_T5_P3, COH_gamma_T5_P3])
            st.success(diagnosis_anx)
        
            
        
        
        st.markdown('---')

    with tabs[2]:

    
        st.header('Anxiety Identification ')
    
        st.markdown('---')
     
    
        # Create a dictionary to store the user's answers
        
        # Create the form using Streamlit widgets
        st.write("Generalized Anxiety Disorder Diagnostic Criteria")
        q1 = st.radio("1. Do you experience excessive anxiety and worry about a number of events or activities?", ('Yes', 'No'))
        q2 = st.radio("2. Has this anxiety and worry been occurring more days than for at least 6 months?", ('Yes', 'No'))
        q3 = st.radio("3. Do you find it difficult to control the worry?", ('Yes', 'No'))
        st.write("4. Have you experienced three or more of the following symptoms for at least 6 months?")
        s1 = st.checkbox("Restlessness or feeling keyed up or on edge")
        s2 = st.checkbox("Being easily fatigued")
        s3 = st.checkbox("Difficulty concentrating or mind going blank")
        s4 = st.checkbox("Irritability")
        s5 = st.checkbox("Muscle tension")
        s6 = st.checkbox("Sleep disturbance (difficulty falling or staying asleep, or restless, unsatisfying sleep)")
        q4 = st.radio("5. Are these symptoms causing clinically significant distress or impairment in social, occupational, or other important areas of functioning?", ('Yes', 'No'))
        q5 = st.radio("6. Is the disturbance not attributable to the physiological effects of a substance or another medical condition?", ('Yes', 'No'))
        q6 = st.radio("7. Has the disturbance not been better explained by another mental disorder?", ('Yes', 'No'))
        q7 = st.radio("8. Do you experience anxiety or worry about having panic attacks in panic disorder?", ('Yes', 'No'))
        q8 = st.radio("9. Do you experience negative evaluation in social anxiety disorder (social phobia)?", ('Yes', 'No'))
        q9 = st.radio("10. Do you experience reminders of traumatic events in posttraumatic stress disorder?", ('Yes', 'No'))
        
        q_list=[q1,q2,q3,q4,q5,q6,q7,q8,q9]
        new_listq = [int(x == 'Yes') for x in q_list]
        sum_q=sum(new_listq)
    
        s_list=[s1,s2,s3,s4,s5,s6]
        new_lists = [int(x == 'Yes') for x in s_list]
        sum_s=sum(new_lists)
    
    
        
        
        # Create a button to submit the form and display the results
        if st.button("Submit"):
            # Check if the criteria for Generalized Anxiety Disorder are met
            if sum_q >1:
                if sum_s > 2 :
                    st.write("You may have Generalized Anxiety Disorder.")
                elif sum_q > 2 :
                    st.write("You may have Generalized Anxiety Disorder.")                
                else: 
                    st.write("You might have symptoms Anxiety Disorder but it is less likely that you are suffering from it .")
            else:
                st.write("You do not meet the criteria for Generalized Anxiety Disorder.")

#--------------------------------------------------------------------------------------    
elif selected == 'Depressive Disorder':
    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:
        
        import streamlit as st
        
        # Set page title and header
        st.title("Depressive Disorder")
        
        # Display introduction
        st.header("Introduction")
        st.write("Depressive Disorder, also known as Major Depressive Disorder (MDD), is a mental health disorder characterized by persistent feelings of sadness, loss of interest, and a lack of pleasure in everyday activities. It affects how you feel, think, and behave and can lead to a variety of emotional and physical problems.")
        
        # Display symptoms
        st.header("Symptoms")
        st.write("The symptoms of Depressive Disorder can vary from person to person, but common symptoms include:")
        st.write("- Persistent feelings of sadness, anxiety, or emptiness")
        st.write("- Loss of interest or pleasure in hobbies and activities")
        st.write("- Fatigue, lethargy, and decreased energy")
        st.write("- Difficulty sleeping or oversleeping")
        st.write("- Changes in appetite and weight")
        st.write("- Feelings of worthlessness or guilt")
        st.write("- Difficulty thinking, concentrating, or making decisions")
        st.write("- Recurrent thoughts of death or suicide")
        
        # Display causes
        st.header("Causes")
        st.write("The exact cause of Depressive Disorder is unknown, but several factors may contribute to its development, including:")
        st.write("- Genetics and family history")
        st.write("- Brain chemistry and hormones")
        st.write("- Life events, such as trauma or loss")
        st.write("- Chronic illness or medical conditions")
        st.write("- Substance abuse")
        
        # Display treatment options
        st.header("Treatment")
        st.write("Depressive Disorder is treatable, and there are several effective treatment options available, including:")
        st.write("- Psychotherapy, such as Cognitive Behavioral Therapy (CBT)")
        st.write("- Medications, such as antidepressants")
        st.write("- Lifestyle changes, such as exercise and stress reduction techniques")
        st.write("- Alternative therapies, such as acupuncture and yoga")
        
        # Display conclusion
        st.header("Conclusion")
        st.write("Depressive Disorder is a common and serious mental health condition that affects millions of people worldwide. With proper treatment and support, most people with Depressive Disorder can achieve a full recovery and live fulfilling lives.")

    with tabs[1]:
        # page title
        st.title('Depressive Disorder')
        st.markdown('> Enter the PSD and FC values for Depression prediction .')
        st.markdown('---')
    
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        
        with col1:
            alpha_T4 = st.text_input('alpha_T4')
            COH_alpha_F8_T4 = st.text_input('COH_alpha_F8_T4')
            COH_alpha_P4_O2 = st.text_input('COH_alpha_P4_O2')
            COH_alpha_Pz_P4 = st.text_input('COH_alpha_Pz_P4')
            COH_alpha_T5_T6 = st.text_input('COH_alpha_T5_T6')
    
        with col2:
            beta_T3 = st.text_input('beta_T3')
            
            COH_beta_F8_O1 = st.text_input('COH_beta_F8_O1')
            COH_beta_P3_O2 = st.text_input('COH_beta_P3_O2')
            COH_theta_F7_T6 = st.text_input('COH_theta_F7_T6')
            COH_theta_FP1_O2 = st.text_input('COH_theta_FP1_O2')
    
        with col3:
            COH_theta_T3_P4 = st.text_input('COH_theta_T3_P4')
            COH_theta_T5_P3 = st.text_input('COH_theta_T5_P3')
            delta_O1 = st.text_input('delta_O1')
            delta_O2 = st.text_input('delta_O2')
            delta_T5 = st.text_input('delta_T5')
            
        #code for prediction
        
       
        diagnosis_dep = ''
        # creating a button for prediction
        #st.markdown('---')
                
        if st.button('Depression Test '):
            diagnosis_dep = Depression_Prediction([delta_O1, COH_alpha_Pz_P4, COH_theta_F7_T6, delta_O2, COH_alpha_T5_T6, COH_alpha_F8_T4, COH_beta_F8_O1, COH_theta_FP1_O2, COH_theta_T5_P3, COH_theta_T3_P4, alpha_T4, COH_alpha_P4_O2, delta_T5, beta_T3, COH_beta_P3_O2])
            st.success(diagnosis_dep)
        st.markdown('---')
                        
    with tabs[2]:    
        st.header('Depression Checker')
        st.markdown('---')
    
        def check_depression(symptoms):
            """
            Returns True if the user meets the diagnostic criteria for a major depressive episode
            based on their symptoms, False otherwise.
            """
            int_list = [int(b) for b in symptoms]
    
            num_symptoms = sum(int_list)
            if num_symptoms < 3:
                print('1')
                return False
            
            if symptoms[0] == True or symptoms[1] == True:
                print('2')
                if num_symptoms >= 3:
                    print('6')
                    return True
            elif num_symptoms >= 5:
                print('7')
                return True
            else:
                print('8')
                return False
        
        st.title("Major Depressive Disorder Diagnosis")
        
        st.write("Please answer the following questions to see if you meet the diagnostic criteria for a major depressive episode.")
        
        depressed_mood = st.checkbox("1. Have you experienced depressed mood most of the day, nearly every day, for at least two weeks?")
        loss_of_interest = st.checkbox("2. Have you lost interest or pleasure in nearly all activities for at least two weeks?")
        weight_change = st.checkbox("3. Have you experienced a significant change in weight or appetite in the past month?")
        insomnia = st.checkbox("4. Do you experience insomnia or hypersomnia nearly every day?")
        psychomotor = st.checkbox("5. Do you experience psychomotor agitation or retardation nearly every day?")
        fatigue = st.checkbox("6. Do you feel fatigued or experience loss of energy nearly every day?")
        worthlessness = st.checkbox("7. Do you experience feelings of worthlessness or excessive or inappropriate guilt nearly every day?")
        concentration = st.checkbox("8. Do you have difficulty thinking or concentrating nearly every day?")
        suicidal = st.checkbox("9. Do you have recurrent thoughts of death, suicide, or have attempted suicide?")
        duration = st.checkbox("10. Have these symptoms persisted for at least two weeks and caused significant distress or impairment in social, occupational, or other areas of functioning?")
        
        symptoms = [depressed_mood, loss_of_interest, weight_change, insomnia, psychomotor, fatigue, worthlessness, concentration, suicidal, duration]
        
        if st.button("Check for Depression"):
            if check_depression(symptoms)== True:
                st.write("Based on your symptoms, you may be experiencing a major depressive episode. Please seek professional help.")
            else:
                st.write("Your symptoms do not meet the diagnostic criteria for a major depressive episode. However, if you are still concerned, please seek professional help.")

#---------------------------------------------
    
#------------------------------------------------------------------------------------------    
elif selected == 'Alcohol addiction':

    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:
        # page title
        
        
        
        import streamlit as st

        # Page title
        st.title("Alcohol Use Disorder")
        
        # Introduction
        st.header("Introduction")
        st.write("Alcohol use disorder (AUD) is a chronic relapsing brain disorder characterized by compulsive alcohol use, loss of control over alcohol intake, and a negative emotional state when not using.")
        
        # Symptoms
        st.header("Symptoms")
        st.write("The symptoms of AUD can range from mild to severe and may include:")
        st.markdown("* Drinking more or longer than intended")
        st.markdown("* Unsuccessful attempts to cut down or stop drinking")
        st.markdown("* Spending a lot of time drinking or recovering from its effects")
        st.markdown("* Craving alcohol")
        st.markdown("* Continued use of alcohol despite its negative effects on relationships, work, or other important aspects of life")
        st.markdown("* Developing a tolerance to alcohol")
        st.markdown("* Experiencing withdrawal symptoms when not drinking")
        
        # Causes
        st.header("Causes")
        st.write("The causes of AUD are complex and include a combination of genetic, environmental, and social factors. Some of the risk factors for developing AUD include:")
        st.markdown("* Family history of alcohol use disorder")
        st.markdown("* Exposure to stress or trauma")
        st.markdown("* Mental health disorders such as depression or anxiety")
        st.markdown("* Peer pressure")
        st.markdown("* Social and cultural norms that encourage heavy drinking")
        
        # Treatment
        st.header("Treatment")
        st.write("AUD is treatable and there are a variety of treatment options available, including:")
        st.markdown("* Medications that can help reduce cravings and withdrawal symptoms")
        st.markdown("* Behavioral therapies that can help individuals change their thoughts and behaviors related to alcohol use")
        st.markdown("* Support groups such as Alcoholics Anonymous")
        st.markdown("* Inpatient or outpatient rehabilitation programs")
        
        # Conclusion
        st.header("Conclusion")
        st.write("Alcohol use disorder is a serious condition that can have a significant impact on an individual's life. With the right treatment and support, however, recovery is possible.")

    with tabs[1]:
        st.title('Alcohol Addiction Test ')
        st.markdown('> Enter the PSD and FC values for Alchoholic Addiction prediction .')
        st.markdown('---')
    
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        
    
        
        with col1:
            COH_alpha_FP2_O2 = st.text_input('COH_alpha_FP2_O2')
            COH_alpha_P4_T6 = st.text_input('COH_alpha_P4_T6')
            COH_alpha_Pz_T6 = st.text_input('COH_alpha_Pz_T6')
            COH_alpha_T3_T4 = st.text_input('COH_alpha_T3_T4')
            COH_highbeta_O1_O2 = st.text_input('COH_highbeta_O1_O2')
    
    
        with col2:
            beta_FP1 = st.text_input('beta_FP1')
            beta_T3 = st.text_input('beta_T3')
            COH_delta_C3_Cz = st.text_input('COH_delta_C3_Cz')
            COH_delta_O1_O2 = st.text_input('COH_delta_O1_O2')
            COH_delta_T6_O1 = st.text_input('COH_delta_T6_O1')
    
        with col3:
            gamma_F8 = st.text_input('gamma_F8')
            gamma_P3 = st.text_input('gamma_P3')
            gamma_T4 = st.text_input('gamma_T4')
            gamma_T6 = st.text_input('gamma_T6')
            gamma_C3 = st.text_input('gamma_C3')
            
        
        #st.markdown('---')
                
        #code for prediction
        
       
        
       
        
        diagnosis = ''
        # creating a button for prediction
        
        if st.button('Alchohol Use Test Result '):
            diagnosis = Alchohol_Prediction([beta_FP1, gamma_T4, gamma_F8, COH_delta_O1_O2, COH_highbeta_O1_O2, beta_T3, COH_alpha_P4_T6, COH_alpha_Pz_T6, gamma_P3, COH_alpha_T3_T4, COH_delta_C3_Cz, COH_alpha_FP2_O2, gamma_T6, COH_delta_T6_O1, gamma_C3])
            st.success(diagnosis)    
        st.markdown('---')
    



        st.markdown('---')
    
        
    
    with tabs[2]:
        def alcohol_use_disorder():
            st.write("# Alcohol Use Disorder")
            st.write("Answer the following questions with Yes or No:")
            st.markdown('---')
    
            # Questions
            q1 = st.selectbox("1. Have you consumed alcohol in larger amounts or for a longer period than you intended?", ['Yes', 'No'])
            q2 = st.selectbox("2. Have you tried to cut down or stop drinking alcohol but found it difficult or unsuccessful?", ['Yes', 'No'])
            q3 = st.selectbox("3. Have you spent a lot of time drinking alcohol or recovering from its effects?", ['Yes', 'No'])
            q4 = st.selectbox("4. Have you experienced strong cravings or a strong urge to drink alcohol?", ['Yes', 'No'])
            q5 = st.selectbox("5. Have you continued to drink alcohol despite it causing or worsening physical or psychological problems?", ['Yes', 'No'])
            q6 = st.selectbox("6. Have you reduced or stopped participating in important social, occupational, or recreational activities because of alcohol use?", ['Yes', 'No'])
            q7 = st.selectbox("7. Have you continued to drink alcohol despite knowing that it has caused or worsened problems with family, friends, or other people?", ['Yes', 'No'])
            q8 = st.selectbox("8. Have you experienced withdrawal symptoms when you stopped or reduced alcohol use (such as tremors, nausea, sweating, or anxiety)?", ['Yes', 'No'])
            q9 = st.selectbox("9. Have you needed to drink more alcohol than before to achieve the desired effect (tolerance)?", ['Yes', 'No'])
            q10 = st.selectbox("10. Have you experienced unsuccessful efforts to quit or cut back on alcohol use in the past?", ['Yes', 'No'])
            
            
            list_q =[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
            new_list = [int(x == 'Yes') for x in list_q]
            sum_q=sum(new_list)
    
            
            
            
            # Criteria for Alcohol Use Disorder
            if sum_q>2:
                duration = st.slider("How long have you experienced these symptoms (in months)?", min_value=1, max_value=120, step=1, value=12)
                if duration >= 12:
                    resultt=("Based on your answers and duration of symptoms, it may indicate a diagnosis of Alcohol Use Disorder. However, a proper diagnosis can only be made by a qualified mental health professional after a thorough evaluation.")
                else:
                    resultt=("The duration of symptoms should be at least 12 months to meet the criteria for Alcohol Use Disorder.")
            else:
                    resultt=("You do not meet the criteria for Alcohol Use Disorder.")
            
            # Reset button
            if st.button("Result"):
                st.write(resultt)
    
    
        alcohol_use_disorder()

#------------------------------------------------------------------------------------------------
    
elif selected == 'Behavioral Addiction':
    
    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:
        
        
        
        # Set page title and heading
        st.title("Behavioral Addiction")
        
        # Define subheadings
        st.header("Overview")
        st.subheader("What is Behavioral Addiction?")
        st.write("Behavioral addiction is a form of addiction that involves engaging in a particular behavior compulsively and repetitively, even if it has negative consequences. These behaviors can range from gambling and gaming to social media and shopping.")
        st.write("Like substance addiction, behavioral addiction can lead to changes in the brain, including increased tolerance, withdrawal symptoms, and an inability to control the behavior.")
        
        st.subheader("Common Forms of Behavioral Addiction")
        st.write("Some common forms of behavioral addiction include:")
        st.write("- Gambling addiction")
        st.write("- Gaming addiction")
        st.write("- Social media addiction")
        st.write("- Shopping addiction")
        st.write("- Internet addiction")
        
        st.header("Causes")
        st.write("The exact causes of behavioral addiction are not fully understood, but it is believed that a combination of genetic, environmental, and psychological factors play a role.")
        st.write("Some of the factors that may contribute to behavioral addiction include:")
        st.write("- Genetics and family history")
        st.write("- Trauma and stress")
        st.write("- Co-occurring mental health disorders, such as anxiety or depression")
        st.write("- Social and environmental factors, such as peer pressure and access to the addictive behavior")
        
        st.header("Symptoms")
        st.write("The symptoms of behavioral addiction can vary depending on the specific behavior and the severity of the addiction. Some common symptoms may include:")
        st.write("- Preoccupation with the behavior")
        st.write("- Difficulty controlling or stopping the behavior")
        st.write("- Continuing to engage in the behavior despite negative consequences, such as financial problems or relationship issues")
        st.write("- Withdrawal symptoms when unable to engage in the behavior")
        st.write("- Tolerance, or the need to engage in the behavior more frequently or for longer periods of time to achieve the same level of satisfaction")
        
        st.header("Treatment")
        st.write("Treatment for behavioral addiction may include a combination of therapy, medication, and lifestyle changes. Some common treatment approaches may include:")
        st.write("- Cognitive behavioral therapy (CBT)")
        st.write("- Dialectical behavior therapy (DBT)")
        st.write("- Medications, such as antidepressants or anti-anxiety medications")
        st.write("- Support groups, such as Gamblers Anonymous or Online Gamers Anonymous")
        st.write("- Lifestyle changes, such as limiting access to the addictive behavior or finding alternative activities to engage in")
        
        st.header("Conclusion")
        st.write("Behavioral addiction is a serious condition that can have a significant impact on an individual's life. If you or someone you know is struggling with behavioral addiction, it is important to seek help from a qualified mental health professional.")

        
        
        
    with tabs[1]:
    
        # page title
        st.title('Behavioral Addiction')
        
        st.markdown('> Enter the PSD and FC values for Behavoral Addiction prediction .')
        st.markdown('---')
    
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        with col1:    
            COH_alpha_T3_T5 = st.text_input('COH_alpha_T3_T5')
            COH_alpha_O1_O2 = st.text_input('COH_alpha_O1_O2')
            COH_alpha_F8_O2 = st.text_input('COH_alpha_F8_O2')
            COH_alpha_Fz_T5 = st.text_input('COH_alpha_Fz_T5')
            COH_alpha_T5_P3 = st.text_input('COH_alpha_T5_P3')
        with col2:
            COH_alpha_T3_T6 = st.text_input('COH_alpha_T3_T6')
            COH_alpha_T4_T5 = st.text_input('COH_alpha_T4_T5')
            COH_beta_F8_O1 = st.text_input('COH_beta_F8_O1')
            COH_beta_F8_O2 = st.text_input('COH_beta_F8_O2')
            COH_theta_T5_P3 = st.text_input('COH_theta_T5_P3')
    
        with col3:
    
            delta_F8 = st.text_input('delta_F8')
            
            COH_delta_T3_C3 = st.text_input('COH_delta_T3_C3')
            COH_delta_P3_O2 = st.text_input('COH_delta_P3_O2')
            COH_delta_F3_T3 = st.text_input('COH_delta_F3_T3')
            COH_delta_F8_T4 = st.text_input('COH_delta_F8_T4')
        
        #st.markdown('---')
                
        #code for prediction
        diagnosis_bl = ''
        # creating a button for prediction
         
        
        
        
        
        
        if st.button('Behavioral Addiction Test '):
            diagnosis_bl = Behavioral_addiction_Prediction([COH_alpha_T3_T5, COH_theta_T5_P3, COH_alpha_O1_O2, COH_alpha_F8_O2, delta_F8, COH_delta_T3_C3, COH_delta_P3_O2, COH_alpha_Fz_T5, COH_beta_F8_O2, COH_delta_F3_T3, COH_alpha_T3_T6, COH_beta_F8_O1, COH_alpha_T5_P3, COH_alpha_T4_T5, COH_delta_F8_T4])
            st.success(diagnosis_bl)
                
        
        st.markdown('---')
    
    with tabs[2]:        
        st.header("Behavioral Addiction Assessment")
        st.markdown('---')
    
        q1 = st.radio("1. Have you engaged in a behavior in larger amounts or for a longer period than you intended?", ('Yes', 'No'))
        q2 = st.radio("2. Have you tried to cut down or stop the behavior but found it difficult or unsuccessful?", ('Yes', 'No'))
        q3 = st.radio("3. Have you spent a lot of time engaging in the behavior or recovering from its effects?", ('Yes', 'No'))
        q4 = st.radio("4. Have you experienced strong cravings or a strong urge to engage in the behavior?", ('Yes', 'No'))
        q5 = st.radio("5. Have you continued to engage in the behavior despite it causing or worsening physical or psychological problems?", ('Yes', 'No'))
        q6 = st.radio("6. Have you reduced or stopped participating in important social, occupational, or recreational activities because of the behavior?", ('Yes', 'No'))
        q7 = st.radio("7. Have you continued to engage in the behavior despite knowing that it has caused or worsened problems with family, friends, or other people?", ('Yes', 'No'))
        q8 = st.radio("8. Have you experienced withdrawal symptoms when you stopped or reduced engagement in the behavior (such as irritability, restlessness, or anxiety)?", ('Yes', 'No'))
        q9 = st.radio("9. Have you needed to engage in the behavior more often or for longer periods of time to achieve the desired effect (tolerance)?", ('Yes', 'No'))
        q10 = st.radio("10. Have you experienced unsuccessful efforts to quit or cut back on engagement in a behavior in the past?", ('Yes', 'No'))
        st.markdown("---")
        list_q =[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        new_list = [int(x == 'Yes') for x in list_q]
        sum_q=sum(new_list)
        duration = st.slider("How long have you experienced these symptoms (in months)?", min_value=1, max_value=120, step=1, value=12)
        st.markdown("---")
        st.subheader("Assessment : ")    
        if sum_q >2:
            
            
            if duration>=12:
                st.write("Based on your responses, you may have a Behavioral Addiction. Please consult a qualified mental health professional for a proper diagnosis.")
            else:
                st.write("The symptoms need to be present for at least 12 months to meet the diagnostic criteria for Behavioral Addiction.")
        else:
            st.write("You do not meet the diagnostic criteria for Behavioral Addiction.")
    
        
#------------------------------------------------------------------------------    
elif selected == 'Trauma & Stress related Disorder':
    
    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:

        # Set page title
        
        # Create headings
        st.title("Trauma and Stressor-Related Disorders")
        st.header("Overview")
        st.subheader("What are Trauma and Stressor-Related Disorders?")
        st.write("Trauma and Stressor-Related Disorders are a group of mental disorders that may develop after a person experiences or witnesses a traumatic or stressful event. These disorders can be triggered by a range of events, including combat, sexual or physical assault, natural disasters, or the sudden loss of a loved one.")
        
        st.subheader("Types of Trauma and Stressor-Related Disorders")
        st.write("There are several types of Trauma and Stressor-Related Disorders, including:")
        st.write("- Acute Stress Disorder")
        st.write("- Post-Traumatic Stress Disorder (PTSD)")
        st.write("- Adjustment Disorders")
        st.write("- Reactive Attachment Disorder")
        st.write("- Disinhibited Social Engagement Disorder")
        
        st.header("Symptoms")
        st.write("Symptoms of Trauma and Stressor-Related Disorders may vary depending on the type of disorder, but common symptoms include:")
        st.write("- Intrusive thoughts or memories of the traumatic event")
        st.write("- Avoidance of people or places that may trigger memories of the event")
        st.write("- Negative changes in mood or thoughts")
        st.write("- Changes in physical and emotional reactions")
        st.write("- Feelings of detachment or emotional numbness")
        
        st.header("Treatment")
        st.write("Treatment for Trauma and Stressor-Related Disorders may include a combination of therapy, medication, and support groups. Therapy may include cognitive-behavioral therapy, exposure therapy, or eye movement desensitization and reprocessing (EMDR). Medication may include antidepressants or anti-anxiety medication.")
        
        st.header("Conclusion")
        st.write("Trauma and Stressor-Related Disorders can have a significant impact on a person's daily life, but with the right treatment and support, recovery is possible. If you or someone you know is struggling with symptoms of a Trauma and Stressor-Related Disorder, it is important to seek help from a mental health professional.")
    
        
    with tabs[1]:
            
        # page title
        st.title('Trauma and Stress Related disorders Test ')
        st.markdown('> Enter the PSD and FC values for Trauma and Stress prediction .')
        st.markdown('---')
    
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        with col2:
            beta_FP1 = st.text_input('beta.FP1')
            beta_FP2 = st.text_input('beta.FP2')
        with col1:
            COH_alpha_F7_T6 = st.text_input('COH.alpha.F7.T6')
            COH_alpha_F8_T4 = st.text_input('COH.alpha.F8.T4')
            COH_alpha_FP2_F8 = st.text_input('COH.alpha.FP2.F8')
            
            COH_alpha_Fz_F4 = st.text_input('COH.alpha.Fz.F4')
            COH_alpha_O1_O2 = st.text_input('COH.alpha.O1.O2')
            
        with col2:    
            COH_beta_FP2_O1 = st.text_input('COH.beta.FP2.O1')
            COH_beta_FP2_F8 = st.text_input('COH.beta.FP2.F8')
            highbeta_O1 = st.text_input('highbeta.O1')
        
        with col3:
            COH_delta_F7_T3 = st.text_input('COH.delta.F7.T3')
            COH_delta_FP1_F8 = st.text_input('COH.delta.FP1.F8')
            COH_delta_FP2_F7 = st.text_input('COH.delta.FP2.F7')
            COH_delta_P3_O2 = st.text_input('COH.delta.P3.O2')
            delta_T5 = st.text_input('delta.T5')
        
        diagnosis_tr = ''
        # creating a button for prediction
         
        if st.button('Trauma and Stress Test '):
            diagnosis_tr = Trauma_Prediction([COH_alpha_FP2_F8, COH_delta_FP2_F7, COH_alpha_F7_T6, delta_T5, COH_beta_FP2_F8, COH_delta_P3_O2, COH_alpha_F8_T4, beta_FP2, COH_beta_FP2_O1, COH_alpha_O1_O2, highbeta_O1, COH_delta_FP1_F8, COH_delta_F7_T3, beta_FP1, COH_alpha_Fz_F4])
            st.success(diagnosis_tr)
                  
          
            
          
        
        
        st.markdown('---')
    with tabs[2]:
            
        st.header("Trauma- and Stressor-Related Disorder Screening")
        st.markdown('---')
        
        q1 = st.radio("1. Have you been exposed to a traumatic or stressful event (such as combat, sexual violence, or a natural disaster)?", ("Yes", "No"))
        
        q2 = st.radio("2. Have you experienced intrusive symptoms related to the traumatic or stressful event (such as flashbacks, nightmares, or distressing memories)?", ("Yes", "No"))
        
        q3 = st.radio("3. Have you experienced avoidance symptoms related to the traumatic or stressful event (such as avoiding thoughts, feelings, or reminders of the event)?", ("Yes", "No"))
        
        q4 = st.radio("4. Have you experienced negative alterations in mood or cognition related to the traumatic or stressful event (such as persistent negative beliefs or emotions, self-blame, or feelings of detachment)?", ("Yes", "No"))
        
        q5 = st.radio("5. Have you experienced marked alterations in arousal and reactivity related to the traumatic or stressful event (such as irritable behavior, hypervigilance, or exaggerated startle response)?", ("Yes", "No"))
        
        q6 = st.radio("6. Have these symptoms been present for at least one month?", ("Yes", "No"))
        
        q7 = st.radio("7. Have these symptoms caused clinically significant distress or impairment in social, occupational, or other important areas of functioning?", ("Yes", "No"))
        
        q8 = st.radio("8. Has the disturbance not been attributable to the physiological effects of a substance or another medical condition?", ("Yes", "No"))
        
        q9 = st.radio("9. Has the disturbance not been better explained by another mental disorder?", ("Yes", "No"))
        
        q10 = st.radio("10. Have the symptoms persisted for more than six months after the traumatic or stressful event (if the event occurred more than six months ago)?", ("Yes", "No"))
    
        list_q =[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        new_list = [int(x == 'Yes') for x in list_q]
        sum_q=sum(new_list)
        st.markdown("---")
        st.subheader("Assessment : ")    
        
        if sum_q>2:
            if q6 == 'Yes':
                st.write("Based on your responses, it is possible that you have Trauma- and Stressor-Related Disorder. It is important to seek help from a qualified mental health professional for a proper diagnosis and treatment.")
            elif q10 == 'Yes':
                st.write("Based on your responses, it is highly possible that you have Trauma- and Stressor-Related Disorder. It is important to seek help from a qualified mental health professional for a proper diagnosis and treatment.")
            
            
            else:
                st.write("Based on your responses, it is less likely that you have Trauma- and Stressor-Related Disorder.The symptoms should at least last a month . However, if you are still concerned, it is recommended to seek help from a qualified mental health professional for further evaluation.")
        else:
            st.write("Based on your responses, it is doesn't seem that you have Trauma- and Stressor-Related Disorder. However, if you are still concerned, it is recommended to seek help from a qualified mental health professional for further evaluation.")
        

#-------------------------------------------------------------------------------------
    
elif selected == 'Schizophrenia':
    tab_titles=['   Description  ','   EEG Based Assessment   ','   Self Assessment   ']
    tabs=st.tabs(tab_titles)
    with tabs[0]:
        # Define page title
        st.title('Schizophrenia')
        
        # What is Schizophrenia?
        st.subheader('What is Schizophrenia?')
        st.write('Schizophrenia is a chronic and severe mental disorder that affects how a person thinks, feels, and behaves. It is a complex condition that can involve a range of symptoms and can be difficult to diagnose.')
        
        # Symptoms of Schizophrenia
        st.header('Symptoms of Schizophrenia')
        st.write('Some of the most common symptoms of schizophrenia include hallucinations (seeing or hearing things that are not there), delusions (holding false beliefs that are not based in reality), disorganized thinking and speech, and difficulty with social interactions and communication.')
        
        # Diagnosis of Schizophrenia
        st.header('Diagnosis of Schizophrenia')
        st.write('Schizophrenia is typically diagnosed in the late teenage years or early adulthood, and it affects men and women equally. It is a lifelong condition, but with proper treatment, many people with schizophrenia are able to manage their symptoms and lead fulfilling lives.')
        
        # Causes of Schizophrenia
        st.header('Causes of Schizophrenia')
        st.write('The exact causes of schizophrenia are not fully understood, but research has shown that it may be related to a combination of genetic, environmental, and neurological factors. Some potential risk factors for schizophrenia include a family history of the disorder, certain prenatal complications or infections, and exposure to stress or trauma.')
        
        # Treatment of Schizophrenia
        st.header('Treatment of Schizophrenia')
        st.write('Treatment for schizophrenia typically involves a combination of medication, therapy, and support from family and healthcare professionals. Antipsychotic medications can be effective in reducing symptoms, while therapy can help individuals with schizophrenia learn coping skills and improve their social functioning.')
    with tabs[1]:
        # page title
        st.title('Schizophrenia')
        st.markdown('> Enter the PSD and FC values for Schizophrenia prediction .')
        st.markdown('---')
       
        #getting the input data from the user 
        
        col1 , col2 ,col3=st.columns(3)
        
        with col1:
            COH_alpha_Cz_O2 = st.text_input('COH.alpha.Cz.O2')
        with col1:
            COH_alpha_F7_T6 = st.text_input('COH.alpha.F7.T6')
        with col1:
            COH_alpha_F8_O2 = st.text_input('COH.alpha.F8.O2')
        with col1:
            COH_alpha_P4_O2 = st.text_input('COH.alpha.P4.O2')
        with col1:
            COH_alpha_T4_P4 = st.text_input('COH.alpha.T4.P4')
        
        with col2:
        
            COH_delta_F7_O2 = st.text_input('COH.delta.F7.O2')
            COH_delta_FP1_O1 = st.text_input('COH.delta.FP1.O1')
            COH_theta_F7_T6 = st.text_input('COH.theta.F7.T6')
            COH_theta_T3_T6 = st.text_input('COH.theta.T3.T6')
            COH_theta_T5_P3 = st.text_input('COH.theta.T5.P3')
        
        with col3:
            COH_beta_F8_T4 = st.text_input('COH.beta.F8.T4')
            delta_O1 = st.text_input('delta.O1')
            delta_O2 = st.text_input('delta.O2')
            delta_T5 = st.text_input('delta.T5')
            delta_T6 = st.text_input('delta.T6')
                
        #code for prediction
        
       
        diagnosis = ''
        # creating a button for prediction
        
        if st.button('Schizophrenia Test Result '):
            diagnosis = Schizophrenia_Prediction([delta_T5, delta_O1, COH_theta_T3_T6, delta_O2, delta_T6, COH_theta_T5_P3, COH_delta_FP1_O1, COH_alpha_Cz_O2, COH_alpha_F8_O2, COH_alpha_P4_O2, COH_alpha_F7_T6, COH_theta_F7_T6, COH_beta_F8_T4, COH_alpha_T4_P4, COH_delta_F7_O2])
            st.success(diagnosis)
        st.markdown('---')
           
   
    with tabs[2]:
        st.header('Schizophrenia detection based on Questionaire .')
        st.markdown('---')
    
        st.subheader('Please answer the following questions with Yes or No')
    
        
        # question responses
        q1 = st.radio("Have you experienced delusions for a significant portion of time in the past month?", ('Yes', 'No'))
        q2 = st.radio("Have you experienced hallucinations for a significant portion of time in the past month?", ('Yes', 'No'))
        q3 = st.radio("Have you experienced disorganized speech, such as frequent derailment or incoherence, for a significant portion of time in the past month?", ('Yes', 'No'))
        q4 = st.radio("Have you exhibited grossly disorganized or catatonic behavior in the past month?", ('Yes', 'No'))
        q5 = st.radio("Have you experienced negative symptoms, such as diminished emotional expression or avolition, for a significant portion of time in the past month?", ('Yes', 'No'))
        q6 = st.radio("Have you experienced a significant decline in your level of functioning in one or more major areas, such as work or interpersonal relations, since the onset of your symptoms?", ('Yes', 'No'))
        q7 = st.radio("Have you experienced continuous signs of the disturbance for at least 6 months?", ('Yes', 'No'))
        q8 = st.radio("Have you experienced symptoms that meet Criterion A (delusions, hallucinations, or disorganized speech) for at least one month during the 6-month period?", ('Yes', 'No'))
        q9 = st.radio("Have mood episodes (major depressive or manic episodes) been ruled out during (delusions or hallucinations )the active-phase symptoms?", ('Yes', 'No'))
        q10 = st.radio("Has the disturbance been ruled out as attributable to the physiological effects of a substance or another medical condition?", ('Yes', 'No'))
    
    
        list_q =[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        new_list = [int(x == 'Yes') for x in list_q]
        sum_q=sum(new_list)
        st.markdown("---")
    
        
        # button to calculate result
        if st.button('Diagnose'):
            # calculate result based on criteria
            if sum_q > 1:
                if q7 == 'Yes' and q8 == 'Yes' and q10 == 'Yes':
                    result = "The diagnosis of schizophrenia could be confirmed."
                elif q3 == 'Yes' and q4 == 'Yes' and q5 == 'Yes': 
                    result = "It has a high possibility that you are suffering for Schizophrenia."
                else:
                    result = "It could be indicative of schizophrenia."
            else:
                result = "It is unlikely to be indicative of schizophrenia."
            
            # display result
            st.write(result)
        
