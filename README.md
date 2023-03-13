# BoomRoom
Hack Green Secret Nuclear Bunker developments

![Alt text](/media/Bunker_240x240.png?raw=true "Hack Green Bunker Logo")  

<img src="/media/first-full-screen-shot.png" width="320px"/>

BoomRoom is a pilot Raspi program to help Hack Green 'script' events their 'Nuclear Attack experience room'. The intention is that the software can fire off either a test script, or a run (normal-operation) script. The scripts are really just a list of times (in ms) and a function to call. The times are given in elapsed ms, so a time of 1250 would indicate 1250 ms after the start of the script, (1.25 seconds).  

The GPIO is available so that relays, lights, motors etc all all within reach, and the initial brief was to be able to play a 5.1 type sound file which might last for a couple of minutes. We are using a resistive-type touch screen of 480x320, on which we draw 2 buttons. The screen effectively disables the onboard HDMI, so our Raspi is configured for SSH over the network too.

We have used PyGame to do most of the heavy lifting around image loading, sound playing, drawing on the screen surface and event handling.    

Our longer-term intention is to make this more robust and flexible, and encourage other smaller museums and installations to use and help extend the programs. 

<img src="/media/boomroom-default.png" width="256px"/><img src="/media/boomroom-test.png" width="256px"/><img src="/media/boomroom-run.png" width="256px"/>  
  
