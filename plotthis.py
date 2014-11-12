import plotly.plotly as py
from plotly.graph_objs import *
 
myname = 'plotlyid'
mykey = "plotlykey"
 
 
py.sign_in(myname,mykey)
 
x1 =[]
y1 =[]
y2 =[]
y3 =[]
MyAnnotation = []
 
 
f = open("LOGGER26.CSV",'r')
#f = open("smallset.csv",'r')
 
for lines in f:
    data = lines.split(',')
    x1.append(data[0]) 
    y1.append(data[1])
    y2.append(data[2])
    y3.append(data[3].strip())
 
    if len(data)==5:
        print data[4]
        Annotation = {'x':data[0],'y':data[1],'text':data[4] + data[0],'xref':'x','yref':'y','showarrow':True,'arrowhead':7,'bgcolor':'red'}
        MyAnnotation.append(Annotation)
 
 
# (2) Make dictionary linking x and y coordinate lists to 'x' and 'y' keys
#     (mandatory in plotly v.1.0.8 and up)
layout = Layout(
    title="MyEnvi",
     
    annotations=MyAnnotation,
     
    legend=Legend(
        x=100,
        y=1
    ),
    xaxis=XAxis(
        domain=[0, 0.8],
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=True,
        autotick=True,
        ticks='',
        showticklabels=True
    ),
    yaxis=YAxis(
        title="Light",
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=True,
        autotick=True,
        ticks='',
        showticklabels=True
    ),
     
    yaxis2=YAxis(
        title='Barometric',
        showgrid=False,
        titlefont=Font(
            color='#ff7f0e'
        ),
        tickfont=Font(
            color='#ff7f0e'
        ),
        anchor='x',
        overlaying='y',
        side='right'
         
    ),
     
    yaxis3=YAxis(
        showgrid=False,
        title='Temp',
        titlefont=Font(
            color='#087804'
        ),
        tickfont=Font(
            color='#087804'
        ),
        anchor='free',
        overlaying='y',
        side='right',
        position = .9
    ),
  
     
     
)
trace1 = dict(x=x1,y=y1, name='Light')
trace2 = dict(x=x1,y=y2, name= 'Barometric',yaxis='y2')
trace3 = dict(x=x1,y=y3, name='Temp',yaxis='y3')
# (3) Make list of 1 trace, to be sent to Plotly
#     (mandatory in 1.0.8 and up)
data = [trace1,trace2,trace3]
 
fig = Figure(data=data,layout=layout)
 
plot_url = py.plot(fig, filename='MyEnvi')
f.close()
