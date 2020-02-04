import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from flask import Flask, redirect, url_for, request, render_template
from sklearn.preprocessing import LabelEncoder
#import numpy as np
#from sklearn import preprocessing
#import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression



app = Flask(__name__, template_folder='E:/PGDM/sem5/Data_science/product/')
app._static_folder = "E:/PGDM/sem5/Data_science/product/"
@app.route('/begin',methods = ['POST', 'GET'])
def begin():
   if request.method == 'POST':
      user = request.form['art1']
      if(user=="Prediction"):
          return render_template('playstore.html')
      else:
          return render_template('login.html')


@app.route('/success1/<name>')
def success1(name):
    df = pd.read_csv('E:\\PGDM\sem5\\Data_science\\final\\description_csv.csv',engine='python')
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=2, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['Description'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    df = df.reset_index()
    titles = df['Application Name']
    indices = pd.Series(df.index, index=df['Application Name'])
    def recommend(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices]
    names1 = recommend(name).head(6)
    names2 = names1.to_frame(name='Application Name')
    return render_template('output_recommend.html', tables=[names2.to_html(classes='data')], titles=names2.columns.values)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['art1']
      return redirect(url_for('success1',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success1',name = user))

  
@app.route('/success/<name>/<name1>/<name2>/<name3>/<name4>/<name5>/<name6>/<name7>/')
def success(name,name1,name2,name3,name4,name5,name6,name7):
    df = pd.read_csv("E:\\PGDM\\sem5\\Data_science\\final\\Final_Data.csv")
    lb_make = LabelEncoder()
    df['Size'] = lb_make.fit_transform(df['Size'])
    df['Category'] = lb_make.fit_transform(df['Category'])
    df['Time elapsed after the last update'] = lb_make.fit_transform(df['Time elapsed after the last update'])
    df['Required Android Version'] = lb_make.fit_transform(df['Required Android Version'])
    df['content_rating'] = lb_make.fit_transform(df['content_rating'])
    data = [[name1,name2,name,name3,name4,name7,name5,name6]] 
  # Create the pandas DataFrame 
    df2 = pd.DataFrame(data, columns = ['Category','No. of reviews','Rating','Time elapsed after the last update',
                                        'Size','No. of Installations(in 00000s)','Required Android Version',
                                        'content_rating']) 
    df2['Size'] = lb_make.fit_transform(df2['Size'])
    df2['Category'] = lb_make.fit_transform(df2['Category'])
    df2['Time elapsed after the last update'] = lb_make.fit_transform(df2['Time elapsed after the last update'])
    df2['Required Android Version'] = lb_make.fit_transform(df2['Required Android Version'])
    df2['content_rating'] = lb_make.fit_transform(df2['content_rating'])
    y_train = df['Success']
    x_train = df.drop('Success',axis=1)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    ypred =logreg.predict(df2)
    dataframe=pd.DataFrame(ypred, columns=['Successful/Not Successful']) 
    return render_template('output_recommend.html', tables=[dataframe.to_html(classes='data')], titles=dataframe.columns.values)

@app.route('/playstore',methods = ['POST', 'GET'])
def playstore():
   if request.method == 'POST':
      rating = request.form['rating']
      category = request.form['category']
      reviews = request.form['reviews']
      time = request.form['time']
      size = request.form['size']
      version = request.form['version']
      content = request.form['content']
      installs = request.form['installs']
      return redirect(url_for('success',name = rating, name1=category,name2=reviews,name3=time,name4=size,name5=version,name6=content,name7=installs))
   else:
      user = request.args.get('rating')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run()