@echo off&setlocal enabledelayedexpansion
set n=0
for /f "delims=" %%a in ('dir /b "F:\11"') do (
if /i not "%%a"=="22.txt" (
set /a n+=1
set "wj!n!=%%a"
)
)
for /f "tokens=1* delims==" %%a in ('set wj') do (
echo %%b    %%a
)
echo 共有%n%个文件(夹)
set /p "a=请输入变量名:"
set "a=!%a%!"
echo 变量对应的文件(夹)是:%a%
paus