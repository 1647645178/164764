# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:12:43 2019

@author: 16476
"""
#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

#人工数据集生成
np.random.seed(5)
x_data = np.linspace(-1,1,100)  #生成100个点在【-1，1】
y_data = 2*x_data + 1.0 + np.random.randn(*x_data.shape)*0.4

plt.scatter(x_data,y_data)
plt.plot(x_data, 2*x_data + 1.0, color = 'red',linewidth=1)
#plt.show

x = tf.placeholder('float', name='x')
y = tf.placeholder('float', name='y')

def model(x,w,b):
    return tf.multiply(x,w) + b

w = tf.Variable(1.0, name='w0')
b = tf.Variable(0.0, name='b0')

pred = model(x,w,b)

train_epochs = 10
learning_rate = 0.05
loss_function = tf.reduce_mean(tf.square(y-pred))

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for epoch in range(train_epochs):
    for xs,ys in zip(x_data, y_data):
        _, loss = sess.run([optimizer,loss_function], 
                           feed_dict={x:xs,y:ys})
b0temp = b.eval(session=sess)
w0temp = w.eval(session=sess)
plt.plot(x_data,w0temp*x_data + b0temp,color='g')
    
print('w:',sess.run(w))
print('b:',sess.run(b))
plt.show()
sess.close()   