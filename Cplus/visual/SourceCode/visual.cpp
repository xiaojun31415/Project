/*
 * visual.cpp
 *
 *  Created on: Dec 25, 2018
 *      Author: xiaojun
 */
#include <windows.h>
#include <stdio.h>

LRESULT CALLBACK WinSunProc(
    HWND hwnd,
    UINT uMsg,
    WPARAM wParam,
    LPARAM lParam
){
    switch(uMsg)
    {

    case WM_CHAR:
        char szChar[20];
        sprintf(szChar,"Char is %d",wParam);
        MessageBox(hwnd,szChar,"Weixin",0);
        break;
    case WM_LBUTTONDOWN:
        MessageBox(hwnd,"mouse clicked","weixin",0);
        HDC hdc;
        hdc=GetDC(hwnd);
        TextOut(hdc,0,50,"计算机",strlen("计算机"));
        ReleaseDC(hwnd,hdc);
        break;
    case WM_PAINT:
        HDC hDC;
        PAINTSTRUCT ps;
        hDC=BeginPaint(hwnd,&ps);
        TextOut(hDC,0,0,"微信",strlen("微信"));
        EndPaint(hwnd,&ps);
        break;
    case WM_CLOSE:
        if(IDYES==MessageBox(hwnd,"是否真的结束？","weixin",MB_YESNO)){
            DestroyWindow(hwnd);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage((0));
        break;
    default:
        return DefWindowProc(hwnd,uMsg,wParam,lParam);
    }
    return 0;
}
int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    LPSTR LpCmdLine,
    int nCmdShow
){
    WNDCLASS wndcls;
    wndcls.cbClsExtra=0;
    wndcls.cbWndExtra=0;
    wndcls.hbrBackground=(HBRUSH)GetStockObject(BLACK_BRUSH);
    wndcls.hCursor=LoadCursor(NULL,IDC_CROSS);
    wndcls.hIcon=LoadIcon(NULL,IDI_ERROR);
    wndcls.hInstance=hInstance;
    wndcls.lpfnWndProc=WinSunProc;
    wndcls.lpszClassName="Weixin2003";
    wndcls.lpszMenuName=NULL;
    wndcls.style=CS_HREDRAW|CS_VREDRAW;
    RegisterClass(&wndcls);

    HWND hwnd;
    hwnd=CreateWindow("Weixin2003","北京微信科学技术中心",WS_OVERLAPPEDWINDOW,
                      0,0,600,400,NULL,NULL,hInstance,NULL);

    ShowWindow(hwnd,SW_SHOWNORMAL);
    UpdateWindow(hwnd);

    MSG msg;
    while(GetMessage(&msg,NULL,0,0)){
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}

