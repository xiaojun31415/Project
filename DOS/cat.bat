@echo off
echo %~dp0 

for /L %%m IN (0,1,1000) do ( echo %%m 
ping jp%%m.accelerator-china.website )

pause 
