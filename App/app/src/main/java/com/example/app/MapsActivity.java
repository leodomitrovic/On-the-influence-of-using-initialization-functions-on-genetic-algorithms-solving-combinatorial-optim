package com.example.app;

import androidx.annotation.Nullable;
import androidx.annotation.RequiresApi;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.FragmentActivity;

import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.DataSource;
import com.bumptech.glide.load.engine.GlideException;
import com.bumptech.glide.request.RequestListener;
import com.bumptech.glide.request.target.Target;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.maps.android.ui.IconGenerator;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.mapa);
        mapFragment.getMapAsync(this);
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        LatLng location = new LatLng(45.260509, 15.217208);
        Uri uri = Uri.parse("https://firebasestorage.googleapis.com/v0/b/projekt-889e1.appspot.com/o/ius0pkpjHK.jpg?alt=media&token=b7d9ab0c-f280-4db1-896b-2cd75d1fa8e2");
        mMap.moveCamera(CameraUpdateFactory.newLatLng(location));
        ColorDrawable cd = new ColorDrawable(ContextCompat.getColor(MapsActivity.this, R.color.black));
        Glide.with(MapsActivity.this)
                .load(uri.toString())
                .addListener(new RequestListener<Drawable>() {
                    @Override
                    public boolean onLoadFailed(@Nullable GlideException e, Object model, Target<Drawable> target, boolean isFirstResource) {
                        return false;
                    }

                    @Override
                    public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target, DataSource dataSource, boolean isFirstResource) {
                        BitmapDrawable d = (BitmapDrawable) resource;
                        Bitmap b = Bitmap.createScaledBitmap(d.getBitmap(), 84, 84, false);
                        ImageView mImageView = new ImageView(getApplicationContext());
                        IconGenerator mIconGenerator = new IconGenerator(getApplicationContext());
                        mImageView.setImageBitmap(b);
                        mIconGenerator.setContentView(mImageView);
                        Bitmap iconBitmap = mIconGenerator.makeIcon();
                        mMap.addMarker(new MarkerOptions().position(location).title("Ogulin").
                                icon(BitmapDescriptorFactory.fromBitmap(iconBitmap)));
                        return true;
                    }
                })
                .placeholder(cd)
                .centerCrop()
                .preload();
    }
}