<?php

namespace App\Http\Controllers;

use App\Service\GenedisApi;

class IndexController extends Controller 
{
    public function index() {

        $installations = GenedisApi::getInstallations();
        
        $resInstall = [];

        $communes = [];
        $communesLabels = [];


        foreach ($installations as $value){
           
            $prop = GenedisApi::getPropietaireById($value[4]);
            $communeName = $value[1];

            if (!in_array($communeName,$communesLabels)) {

                $communesLabels[] = $value[1];
            }

            
            if (array_key_exists($communeName ,$communes)) {

                $communes[$communeName]['val'] =  $communes[$communeName]['val'] +1;
            } else {

                $communes[$communeName] = ['val' => 1];

            }

            $propName = $prop[0][1];

            if (array_key_exists($propName ,$resInstall))   {

                $resInstall[$propName]['val'] =  $resInstall[$propName]['val'] +1;
                
            } else  {
                $resInstall[$propName] = ['val' => 1];
            } 
          
          
        }



        $labels = array_keys($resInstall);

        $data = [];

        $dataCommune = [];

        foreach($resInstall as $d) {

            $data[] = $d['val'];
        }

        foreach($communes as $d) {

            $dataCommune[] = $d['val'];
        }


        return view('index', compact('labels','data','communesLabels','dataCommune'));
    }
}