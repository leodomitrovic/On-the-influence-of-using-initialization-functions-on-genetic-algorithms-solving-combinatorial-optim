package com.example.app;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;

import java.util.HashMap;
import java.util.Map;

public class Register extends AppCompatActivity {
    EditText e;
    EditText p;
    EditText n;
    Button b;
    FirebaseAuth auth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        e = findViewById(R.id.editTextTextEmailAddress);
        p = findViewById(R.id.editTextTextPassword);
        b = findViewById(R.id.button);
        n = findViewById(R.id.editTextTextPersonName);
        auth = FirebaseAuth.getInstance();

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = e.getText().toString().trim();
                String pass = p.getText().toString().trim();
                String name = n.getText().toString().trim();
                if (!email.equals("") && !pass.equals("") && !name.equals("")) {
                    auth.createUserWithEmailAndPassword(email, pass).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if (task.isSuccessful()) {
                                Toast.makeText(Register.this, "Uspjeh", Toast.LENGTH_SHORT).show();
                                FirebaseFirestore db = FirebaseFirestore.getInstance();
                                Intent intent = getIntent();
                                String tip = intent.getStringExtra("Tip");

                                Map<String, Object> user = new HashMap<>();
                                user.put("ID", auth.getCurrentUser().getUid());
                                user.put("E-mail", email);
                                user.put("Full name", name);
                                user.put("Type", tip);

                                db.collection("Users").add(user).addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
                                    @Override
                                    public void onSuccess(DocumentReference documentReference) {
                                        finish();
                                        startActivity(new Intent(Register.this, Check.class));
                                        //startActivity(new Intent(Register.this, MainActivity.class));
                                    }
                                });
                            } else {
                                Toast.makeText(Register.this, task.getException().toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    });
                }
            }
        });
    }
}