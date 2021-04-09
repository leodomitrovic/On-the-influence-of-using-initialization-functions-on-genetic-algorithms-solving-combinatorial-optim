package com.example.app;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class Login extends AppCompatActivity {
    public EditText e;
    EditText p;
    Button b;
    FirebaseAuth auth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        e = findViewById(R.id.editTextTextEmailAddress2);
        p = findViewById(R.id.editTextTextPassword2);
        b = findViewById(R.id.button2);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                auth = FirebaseAuth.getInstance();
                String email = e.getText().toString().trim();
                String pass = p.getText().toString().trim();
                if (!email.equals("") && !pass.equals("")) {
                    auth.signInWithEmailAndPassword(email, pass).addOnSuccessListener(new OnSuccessListener<AuthResult>() {
                        @Override
                        public void onSuccess(AuthResult authResult) {
                            finish(); //mora
                            startActivity(new Intent(Login.this, Check.class));
                        }
                    });
                }
            }
        });

        TextView t = findViewById(R.id.textView2);
        t.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish(); //---
                Intent i = new Intent(Login.this, Register.class);
                i.putExtra("Tip", "2");
                startActivity(i);
            }
        });
    }
}