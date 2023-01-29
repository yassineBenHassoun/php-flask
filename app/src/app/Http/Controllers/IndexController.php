<?php

namespace App\Http\Controllers;

use App\Service\GenedisApi;

class IndexController extends Controller 
{
    public function index() {

        #dd(GenedisApi::getInstallByPropietaire(1));

        $arr = [

            "nom"=> "Laravel",
            "commune"=> "newYork",
            "capacite"=> 1200.0,
            "anneeInstallation"=> "T.A. 3000",
            "idProprietaire" => 1
        ];
        dd(GenedisApi::registerInstallation($arr));
        //return view('index');
    }
}