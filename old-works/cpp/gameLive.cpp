#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <conio.h>

using namespace std;

short screenX=60, screenY=30,firstGen,randC=0;

vector<vector<bool>> screen, newScreen, oldScreen, nothing, vivodForMakeStructure;
vector<vector<char>> prScreen;
//база структур
vector<vector<bool>> glider={{0,1,0},{1,0,0},{1,1,1}};//1
vector<vector<bool>> block={{1,1},{1,1}};//2
vector<vector<bool>> loaf={{0,1,1,0},{1,0,0,1},{0,1,0,1},{0,0,1,0}};//3
vector<vector<bool>> beehive={{0,1,0},{1,0,1},{1,0,1},{0,1,0}};//4
vector<vector<bool>> tub={{0,1,0},{1,0,1},{0,1,0}};//5
vector<vector<bool>> pond={{0,1,1,0},{1,0,0,1},{1,0,0,1},{0,1,1,0}};//6
vector<vector<bool>> barge={{0,1,0,0},{1,0,1,0},{0,1,0,1},{0,0,1,0}};//7
vector<vector<bool>> boat={{0,1,0},{1,0,1},{0,1,1}};//8
vector<vector<bool>> ship={{1,1,0},{1,0,1},{0,1,1}};//9
vector<vector<bool>> aircraftCarrier={{1,1,0,0},{1,0,0,1},{0,0,1,1}};//10
vector<vector<bool>> longBoat={{0,1,0,0},{1,0,1,0},{0,1,0,1},{0,0,1,1}};//11
vector<vector<bool>> longShip={{1,1,0,0},{1,0,1,0},{0,1,0,1},{0,0,1,1}};//12
vector<vector<bool>> figureEight={{1,1,0,0},{1,1,0,0},{0,0,1,1},{0,0,1,1}};//13

void initScreens(){
    screen.resize(screenY);
    newScreen.resize(screenY);
    oldScreen.resize(screenY);
    
    for (short j = 0; j < screenY; j++) {
        screen[j].resize(screenX, false);
        newScreen[j].resize(screenX, false); 
        oldScreen[j].resize(screenX, true);
    }
    nothing=screen;
    vivodForMakeStructure=nothing;
}

vector<vector<bool>> right(vector<vector<bool>>& arr){
	if (arr.empty() || arr[0].empty()) {
    	return vector<vector<bool>>();
	}
	short rows = arr.size();
    short cols = arr[0].size();
    
    vector<vector<bool>> arrn(cols, vector<bool>(rows, false));
	
	for(short j=0;j<arr.size();j++){
		for(short i=0;i<arr[j].size();i++){
			arrn[i][rows-j-1]=arr[j][i];
		}
	}
	return arrn;
}

vector<vector<bool>> left(vector<vector<bool>>& arr){
	if (arr.empty() || arr[0].empty()) {
    	return vector<vector<bool>>();
	}
	short rows = arr.size();
    short cols = arr[0].size();
    
    vector<vector<bool>> arrn(cols, vector<bool>(rows, false));
	
	for(short j=0;j<arr.size();j++){
		for(short i=0;i<arr[j].size();i++){
			arrn[cols-i-1][j]=arr[j][i];
		}
	}
	return arrn;
}

void generation(){
	for(short j=0;j<screenY;j++){
		for(short i=0;i<screenX;i++){
			srand(time(nullptr)+clock()+randC);
			short a=rand()%firstGen;
			
			if(a==1 || a==0){screen[j][i]=true;}
			else {screen[j][i]=false;}
			
			randC+=a;
		}
	}
}
void header(){
		cout<<"Выберите элемент для размещения из списка:\n1)glider=================2)block\n3)loaf=================4)beehive\n5)tub=====================6)pond\n7)barge===================8)boat\n9)ship=======10)aircraft Carrier\n11)long Ship========12)long Ship\n0)4gliders================p)play\n";
}

void createGladers(){
	screen[0][1]=1;screen[1][2]=1;screen[2][0]=1;screen[2][1]=1;screen[2][2]=1;
	screen[0][screenX-3]=1;screen[1][screenX-4]=1;screen[2][screenX-2]=1;screen[2][screenX-3]=1;screen[2][screenX-4]=1;
	screen[screenY-1][1]=1;screen[screenY-2][2]=1;screen[screenY-3][0]=1;screen[screenY-3][1]=1;screen[screenY-3][2]=1;
	screen[screenY-1][screenX-3]=1;screen[screenY-2][screenX-4]=1;screen[screenY-3][screenX-2]=1;screen[screenY-3][screenX-3]=1;screen[screenY-3][screenX-4]=1;
}

void printScreen(vector<vector<bool>>& screenP){
	short rows=screenP.size();
	short cols=screenP[0].size();
	
	prScreen.resize(rows);
	for (short j = 0; j < rows; j++) {
		prScreen[j].resize(cols, ' ');
	}
	for(short j=0;j<rows;j++){
		for(short i=0;i<cols;i++){
			if(screenP[j][i]){prScreen[j][i]='#';}
			else {prScreen[j][i]=' ';}
			cout<<prScreen[j][i];
		}
		cout<<endl;
	}
}

void isAlive(){
	oldScreen=screen;
	for(short j=0;j<screenY;j++){
		for(short i=0;i<screenX;i++){
			short c=0;
			if(j>=1 && i<(screenX-1)){
				if(screen[j-1][i]==true){c++;}
				if(screen[j-1][i+1]==true){c++;}
			}
			if(j>=1 && i>=1){
				if(screen[j-1][i-1]==true){c++;}
			}
			if(i<(screenX-1)){
				if(screen[j][i+1]==true){c++;}
			}
			if(i>=1){
				if(screen[j][i-1]==true){c++;}
			}
			if(j<(screenY-1) && i<(screenX-1)){
				if(screen[j+1][i]==true){c++;}
				if(screen[j+1][i+1]==true){c++;}
			}
			if(j<(screenY-1) && i>=1){
				if(screen[j+1][i-1]==true){c++;}
			}
			
			if(screen[j][i]){newScreen[j][i]=(c==2 || c==3);}
			else {newScreen[j][i]=(c==3);}
		}
	}
	screen=newScreen;
}

void sovmestit(vector<vector<bool>>& previewScreenn){
	for(short j=0;j<screenY;j++){
		for(short i=0;i<screenX;i++){
		vivodForMakeStructure[j][i]=(screen[j][i] || previewScreenn[j][i]);	
		}
	}
}

void save(vector<vector<bool>>& previewScreenn){
	for(short j=0;j<screenY;j++){
		for(short i=0;i<screenX;i++){
		screen[j][i]=(screen[j][i] || previewScreenn[j][i]);	
		}
	}
}

void makeStructure(vector<vector<bool>>& broadcastArr){
	vector<vector<bool>> arr=broadcastArr;
	vector<vector<bool>> previewScreen=nothing, oldArr=arr;
	
	short x=0,y=0,nx=0,ny=0, lastOper=0;
	
	while(true){
		short rows=arr.size(), cols=arr[0].size();
		
		if(lastOper==5 || lastOper==6){
			previewScreen=nothing;
		}
		
		for(short j=0;j<rows;j++){
			if(lastOper==1 && x>0){
					previewScreen[j+y][x-1]=false;
				}
				else if(lastOper==2){
					previewScreen[j+y][x+cols]=false;
				}
			for(short i=0;i<cols;i++){
				previewScreen[j+y][i+x]=arr[j][i];
				
				if(lastOper==3 && y>0){
					previewScreen[y-1][i+x]=false;
				}
				else if(lastOper==4){
					previewScreen[y+rows][i+x]=false;
				}
			}
		}
		cout<<"\033[H";
		system("clear");
		sovmestit(previewScreen);
		printScreen(vivodForMakeStructure);
		char key=_getch();
		
		switch(key){
			case('d'):
			nx++;
			if(nx<(screenX-cols-1)){
				x=nx;
				lastOper=1;
			}
			else nx--;
			break;
			case('a'):
			nx--;
			if(nx>0){
				x=nx;
				lastOper=2;
			}
			else nx++;
			break;
			case('s'):
			ny++;
			if(ny<(screenY-rows-1)){
				y=ny;
				lastOper=3;
			}
			else ny--;
			break;
			case('w'):
			ny--;
			if(ny>0){
				y=ny;
				lastOper=4;
			}
			else ny++;
			break;
			case('e'):
			if((x+rows)<(screenX-1)&&(y+cols)<(screenY-1)){
				oldArr=arr;
				arr=left(arr);
				lastOper=5;
			}
			break;
			case('r'):
			if((x+rows)<(screenX-1)&&(y+cols)<(screenY-1)){
				oldArr=arr;
				arr=right(arr);
				lastOper=6;
			}
			break;
			case('n'):
			return;
			break;
			case('y'):
			save(previewScreen);
			break;
		}
	}
	
}


int main(int argc, char *argv[]){
	setlocale(LC_ALL, "Russian");
	
	float t=0,T=0;
	
	initScreens();
	
	bool running=true,runn=false;
	string star;
	
		cout<<"Добро пожаловать в игру жизнь\nВыберiте режим(random, make): ";
		cin>>star;
		while(true){
		if(star=="random"){
			while(running){
				cout<<"Введиде знаменатель дроби(2/n), которая показывает, какая часть экрана будет случайным образом изначально заполнена клетками. Число должно быть больше, чем 2.\n"<<"n = ";
			if(cin>>firstGen && firstGen>2){running=false;}
			else{cout<<"Вы ввели не число или введеное вами число меньше или равно двум!\nНажмите enter для повторного ввода";
			cin.clear();
			cin.ignore(3,'/n');
				system("clear");
				}
			}
			generation();
			t=1;
			runn=true;
		}
		else if(star=="make"){
			system("clear");
			bool create=true;
			
			while(create){
				system("clear");
				string button=" ";
				header();
				cin>>button;
				
				if(button=="0" || button=="0 "){
					createGladers();
					T=50000;
					runn=true;
					create=false;
					}
				else if(button=="p" || button=="P" || button=="p " || button=="P "){
					T=50000;
					runn=true;
					create=false;
				}
				else if(button=="1" || button=="1 "){
					makeStructure(glider);
				}
				else if(button=="2" || button=="2 "){
					makeStructure(block);
				}
				else if(button=="3" || button=="3 "){
					makeStructure(loaf);
				}
				else if(button=="4" || button=="4 "){
					makeStructure(beehive);
				}
				else if(button=="5" || button=="5 "){
					makeStructure(tub);
				}
				else if(button=="6" || button=="6 "){
					makeStructure(pond);
				}
				else if(button=="7" || button=="7 "){
					makeStructure(barge);
				}
				else if(button=="8" || button=="8 "){
					makeStructure(boat);
				}
				else if(button=="9" || button=="9 "){
					makeStructure(ship);
				}
				else if(button=="10" || button=="10 "){
					makeStructure(aircraftCarrier);
				}
				else if(button=="11" || button=="11 "){
					makeStructure(longBoat);
				}
				else if(button=="12" || button=="12 "){
					makeStructure(longShip);
				}
				else if(button=="13" || button=="13 "){
					makeStructure(figureEight);
				}
				else if(button=="p" || button=="p " || button=="P" || button=="P "){
					T=50000;
					runn=true;
					create=false;
				}
			}
		}
		
		else {cout<<"this not mode. try again";}
		break;
}

	while(runn){
		system("clear");
		printScreen(screen);
		isAlive();
		sleep(t);
		usleep(T);
		if(oldScreen==newScreen)runn=false;
	}
	
	return 0;
}