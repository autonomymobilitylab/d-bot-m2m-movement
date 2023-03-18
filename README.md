# d-bot-m2m-movement

dbot m2m movement package

## hardware  

Digital AC Servo driver\
ZLTECH ZLAC8015D  
<https://www.manualslib.com/manual/2488201/Zltech-Zlac8015d.html#manual>  


Computing  
Intel NUC  

![Image](./resource/img/hardware_1.jpg)

## installation

```bash
apt-get update  
apt-get install pip  
pip3 install smbus2  
pip3 install python-can[pcan]  
```

## libraries

running motors from Intel Nuc

Credits to rasheeddo for amazing work with zlac8015d
<https://github.com/rasheeddo/ZLAC8015D_python>
<https://github.com/rasheeddo/jmoab-ros>
