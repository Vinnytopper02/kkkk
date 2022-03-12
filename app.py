#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask (__name__)
@app.route('/')
def xyz():
    return render_template('hellohello1.html')
@app.route('/info',methods=['POST'])
def abc():
    if (request.method=='POST'):
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        o=num1+num2
        return render_template('hellohello1.html',total=o)
if __name__=='__main__':
    app.run()


# In[ ]:




