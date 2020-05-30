
# coding: utf-8

# In[41]:


from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file

start = datetime.datetime(2018,12,2)
end = datetime.datetime(2019,3,11)
stock = data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

def inc_dec(close, open):
    if close > open:
        value = "Increase"
    elif close < open:
        value = "Decrease"
    else:
        value = "Equal"
    return value

stock["Status"] = [inc_dec(close, open) for close, open in zip(stock.Close, stock.Open)]

stock["Middle"] = (stock.Open+stock.Close)/2

stock["Height"] = abs(stock.Open-stock.Close)

stock

p = figure(x_axis_type="datetime", width=1000, height=300, responsive = True)
p.title.text = 'Candlestick Chart'
p.grid.grid_line_alpha = 0.3

hours_12 = 12*60*60*1000

p.segment(stock.index, stock.High, stock.index, stock.Low, color="black")

p.rect(stock.index[stock.Status == "Increase"],stock.Middle[stock.Status == "Increase"],
       hours_12, stock.Height[stock.Status == "Increase"], fill_color="#ccffff", line_color="black")

p.rect(stock.index[stock.Status == "Decrease"],stock.Middle[stock.Status == "Decrease"], 
       hours_12, stock.Height[stock.Status == "Decrease"], fill_color="#ff3333", line_color="black")



output_file('BishopsCS.html')
show(p)

