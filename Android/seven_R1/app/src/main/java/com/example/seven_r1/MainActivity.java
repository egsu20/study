package com.example.seven_r1;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {
    LinearLayout baseLayout;
    Button button1;
    boolean flagRed=false, flagGreen=false, flagBlue=false, flagRotate=false, flagScale=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("배경색 바꾸기");

        baseLayout = (LinearLayout)findViewById(R.id.baseLayout);
        button1 = (Button)findViewById(R.id.button1);

    }
    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    public boolean onOptionsItemSelected(MenuItem item){
        switch (item.getItemId()){
            case R.id.itemRed:
                if(flagRed == false) {
                    baseLayout.setBackgroundColor(Color.RED);
                    flagRed = true;
                }
                else {
                    baseLayout.setBackgroundColor(Color.WHITE);
                    flagRed = false;
                }
                return true;
            case R.id.itemGreen:
                if(flagGreen == false) {
                    baseLayout.setBackgroundColor(Color.GREEN);
                    flagGreen = true;
                }
                else {
                    baseLayout.setBackgroundColor(Color.WHITE);
                    flagGreen = false;
                }
                return true;
            case R.id.itemBlue:
                if(flagBlue == false){
                    baseLayout.setBackgroundColor(Color.BLUE);
                    flagBlue = true;
                }
                else {
                    baseLayout.setBackgroundColor(Color.WHITE);
                    flagBlue = false;
                }
                return true;
            case R.id.itemClear:
               baseLayout.setBackgroundColor(Color.WHITE);
               flagBlue = false;
               flagRed = false;
               flagGreen = false;
               return true;
            case R.id.subRotate:
                if(flagRotate == false){
                    button1.setRotation(45);
                    flagRotate = true;
                }
                else{
                    button1.setRotation(0);
                    flagRotate = false;
                }
                return true;
            case R.id.subSize:
                if(flagScale == false){
                    button1.setScaleX(2);
                    flagScale = true;
                }
                else{
                    button1.setScaleX(2);
                    flagScale = false;
                }
                return true;
            case R.id.subClear:
                button1.setScaleX(1);
                button1.setRotation(0);
                return true;
        }
        return false;
    }
    public boolean onCreateOptionsMenu(Menu menu){
        super.onCreateOptionsMenu(menu);
        MenuInflater mInflater = getMenuInflater();
        mInflater.inflate(R.menu.menu1, menu);
        return true;
    }
}