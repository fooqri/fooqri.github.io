---
layout: post
title: "d3 charts - wrapping 'NVD3 Charts' in a web component"
date: 2014-10-17 06:39
comments: true
categories: 
---

In my continued experiments with Polymer, I created a web component that wraps  <a href="http://nvd3.org/" target="_blank">NVD3</a> - a reusable chart library for d3.js.
As part of the activity I ported all of the  <a href="http://nvd3.org/examples/index.html" target="_blank">NVD3 example charts</a> to a web component I am calling _<goddip-charts>_. The component is contained in a <a href="http://www.poggr.com/pekqyTpXDEe:deJoY70GdVx" target="_blank">pogg</a> on <a href="http://www.poggr.com/home/" target="_blank">poggr.com</a>, as this is where I do my experimenting and it allows me to code and serve the project documents in the one place. 

<iframe width="620px" height="320px" src="http://www.poggr.com/pg1GXbi9MBx:dlym9bhp4Lx::49"></iframe>

The above chart is an iframe to <a href="http://www.poggr.com/pg1GXbi9MBx:dlym9bhp4Lx::49" target="_blank">this document</a> The actual element tag used is as follows:

     <goddip-charts  
       class="small-chart-styles"
       chartType="bar"
       context="/pg1GXbi9MBx:deyDCclAEUg::49" 
       css="/pg1GXbi9MBx:dxkNM7ZicfBe::49" >
     </goddip-charts >

To view the uncompiled and unminimized source see (<a href="http://source.poggr.com/pg1GXbi9MBx:dlym9bhp4Lx::49" target="_blank">html document source</a>, <a href="http://source.poggr.com/pg1GXbi9MBx:deyDCclAEUg::49" target="_blank">data document source</a>, and <a href="http://source.poggr.com/pg1GXbi9MBx:dxkNM7ZicfBe::49" target="_blank">style document source</a>).
     
The best way to learn about the _<goddip-charts>_ component is to take a look at its <a href="http://www.poggr.com/pg1GXbi9MBx:dgJXG7boqzSe" target="_blank">README document</a>. This describes how to use each of the charts, reference data, adding styling, etc. You can always view the component <a href="http://source.poggr.com/pg1GXbi9MBx:dlJkI7k9tBe" target="_blank">source</a>. If you have a _poggr.com_ account you can view, clone, and edit _goddip-charts_ using the <a href="http://project.poggr.com/pg1GXbi9MBx" target="_blank">poggr project UI</a>.






