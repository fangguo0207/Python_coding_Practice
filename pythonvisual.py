# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:43:11 2016

@author: FANG
"""




with sns.axes_style("white"):
    g=sns.FacetGrid(tips,row="sex",col="smoker",margin_titles=True,size=2.5)
g.map(plt.scatter,"total_bill","tip",color="#334488",edgecolor="white",lw=.5)
g.set_axis_labels("Total bill (US Dollars)","Tip")
g.set(xticks=[10,30,50],yticks=[2,6,10])
g.fig.subplots_adjust(wspace=.1,hspace=.3)


g=sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

g = sns.PairGrid(iris, hue="species")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend();