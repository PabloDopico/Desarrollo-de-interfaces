package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class CatalogActivity extends AppCompatActivity {

    private Button buttonDetalles;  // añadimos un botón

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);  // establecemos el layout xml de la clase

        Intent intent = new Intent(this, DetailActivity.class);  // asignamos la clase DetailActivity al intent
        buttonDetalles = findViewById(R.id.ButtonDetalle);  // asignamos el Button del xml al butón creado en esta clase

        buttonDetalles.setOnClickListener(new View.OnClickListener() {  // indicamos lo que debe hacer al pulsar el boton
            @Override
            public void onClick(View view) {

                startActivity(intent);  // el botón iniciara la actividad guardada en el intent
            }
        });

    }
}