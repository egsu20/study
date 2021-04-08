package com.example.helloandroid;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.MultiAutoCompleteTextView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ViewFlipper;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.setContentView(R.layout.activity_main);

        Button btnStart, btnStop;
        final ViewFlipper vFlipper;

        btnStart = (Button)findViewById(R.id.btnStart);

        vFlipper = (ViewFlipper)findViewById(R.id.viewFlipper1);
        vFlipper.setFlipInterval(3000);

        btnStart.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){
                vFlipper.startFlipping();
            }
        });
     }
}