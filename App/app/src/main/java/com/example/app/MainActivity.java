package com.example.app;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.location.Location;
import android.media.ExifInterface;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.IOException;
import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class MainActivity extends AppCompatActivity {
    private static final int OPEN_DOCUMENT_REQUEST = 1;
    FirebaseAuth auth;
    FirebaseUser user;
    FirebaseFirestore db;
    String tip;
    ImageView t;
    public static final int GALLERY_ACTIVITY_REQUEST_CODE = 2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        auth = FirebaseAuth.getInstance();
        t = findViewById(R.id.imageView);

        Button b = findViewById(R.id.button4);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent galleryIntent = new Intent();
                galleryIntent.setType("*/*");
                galleryIntent.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(Intent.createChooser(galleryIntent, "Select Photo/Video"), GALLERY_ACTIVITY_REQUEST_CODE);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        user = auth.getCurrentUser();
        db = FirebaseFirestore.getInstance();

        CollectionReference colRef1 = db.collection("Users");
        colRef1.get().addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
            @Override
            public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                for (QueryDocumentSnapshot doc : queryDocumentSnapshots) {
                    String ID = doc.getString("ID");
                    if (doc.getString("ID").equals(user.getUid())) {
                        tip = doc.getString("Type");
                        if (tip.equals("1")) {
                            inflater.inflate(R.menu.menu_admin, menu);
                        } else {
                            inflater.inflate(R.menu.menu, menu);
                        }
                    }
                }
            }
        });
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {
            case R.id.user_data:
                user = auth.getCurrentUser();
                FirebaseFirestore db = FirebaseFirestore.getInstance();

                CollectionReference colRef = db.collection("Users");
                colRef.get().addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
                    @Override
                    public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                        for (QueryDocumentSnapshot doc : queryDocumentSnapshots) {
                            if (doc.getString("ID").equals(user.getUid())) {
                                //finish();
                                String name = doc.getString("Full name");
                                String email = doc.getString("E-mail");
                                String ID = doc.getId();
                                Intent i = new Intent(MainActivity.this, User_data.class);
                                i.putExtra("Ime", name);
                                i.putExtra("E-mail", email);
                                i.putExtra("ID", ID);
                                i.putExtra("Tip", tip);
                                startActivity(i);
                                break;
                                //startActivity(new Intent(Check.this, Login.class));
                            }
                        }
                    }
                });
                return true;
            case R.id.add_admin:
                finish();
                Intent i = new Intent(MainActivity.this, Register.class);
                i.putExtra("Tip", "1");
                startActivity(i);
                return true;
            case R.id.sign_out:
                auth.signOut();
                finish();
                startActivity(new Intent(MainActivity.this, Login.class));
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == GALLERY_ACTIVITY_REQUEST_CODE) {
            if (resultCode != RESULT_OK) return;
            FirebaseStorage storage = FirebaseStorage.getInstance();
            StorageReference storageRef = storage.getReference();
            String AlphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvxyz";
            StringBuilder sb = new StringBuilder(10);
            for (int i = 0; i < 10; i++) {
                int index = (int)(AlphaNumericString.length() * Math.random());
                sb.append(AlphaNumericString.charAt(index));
            }
            StorageReference mountainsRef = storageRef.child(sb.toString() + ".jpg");
            StorageReference mountainImagesRef = storageRef.child(user.getEmail());
            mountainsRef.getName().equals(mountainImagesRef.getName());
            mountainsRef.getPath().equals(mountainImagesRef.getPath());
            Uri uri1 = data.getData();
            UploadTask uploadTask = mountainsRef.putFile(uri1);
            uploadTask.addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception exception) {
                    Toast.makeText(MainActivity.this, exception.toString(), Toast.LENGTH_LONG).show();
                }
            }).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
                @Override
                public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
                    taskSnapshot.getMetadata().getReference().getDownloadUrl().addOnCompleteListener(new OnCompleteListener<Uri>() {
                        @RequiresApi(api = Build.VERSION_CODES.N)
                        @Override
                        public void onComplete(@NonNull Task<Uri> task) {
                            if (task.isSuccessful()) {
                                try {
                                    InputStream in;
                                    TextView o = findViewById(R.id.textView);
                                    in = getContentResolver().openInputStream(uri1);
                                    ExifInterface exif = new ExifInterface(in);
                                    Location loc = new Location("");
                                    float[] latlong = new float[2] ;
                                    if(exif.getLatLong(latlong)){
                                        loc.setLatitude(latlong[0]);
                                        loc.setLongitude(latlong[1]);
                                        o.setText(loc.toString());
                                        //45.260509 15.217208
                                    }
                                    String date = exif.getAttribute(ExifInterface.TAG_DATETIME);
                                    SimpleDateFormat fmt_Exif = new SimpleDateFormat("yyyy:MM:dd HH:mm:ss");
                                    loc.setTime(fmt_Exif.parse(date).getTime());
                                } catch (IOException | ParseException e) {
                                    e.printStackTrace();
                                }
                            } else {
                                Toast.makeText(MainActivity.this, task.getException().toString(), Toast.LENGTH_LONG).show();
                            }
                        }
                    });
                }
            });
        }
    }
}