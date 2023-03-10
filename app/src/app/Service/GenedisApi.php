<?

namespace App\Service;

use GuzzleHttp\Client;

class GenedisApi 
{
    ## api we pass the name of the container 
    private static $uriAllInstall = 'http://api:5000/installations';
    private static $uriInstallPropietaireById = 'http://api:5000/installations/parProprietaire/';
    private static $uriAllProp = "http://api:5000/proprietaires";
    private static $uriPropById = "http://api:5000/proprietaires/";

    
    public static function getInstallations() {

        $client = new Client();
        $res = $client->get(self::$uriAllInstall);

        if ($res->getStatusCode() == 200) {

            return json_decode($res->getBody());
        } 
       
        return null;
    }

    public static function getInstallByPropietaire($id) {
        
        $client = new Client();
        $res = $client->get(self::$uriInstallPropietaireById.$id);

        if ($res->getStatusCode() == 200) {

            return json_decode($res->getBody());
        } 
       
        return null;
     
    }

    public static function registerInstallation (array $data) {

        if (array_key_exists('nom',$data) && array_key_exists('commune',$data) && array_key_exists('capacite',$data) 
            && array_key_exists('anneeInstallation',$data) && array_key_exists('idProprietaire',$data) ) {

            $client = new Client();
         
            $response = $client->request('POST', self::$uriAllInstall, [
                'json' => $data
            ]);

            if ($response->getStatusCode() == 200) {

                $result = [
                    "status" => 200,
                    json_decode($response->getBody())
                ];
                return $result;
            } 
            
        } else {

            return 'array missing values';
        }
    }

    public static function getPropietaires() {

        $client = new Client();
        $res = $client->get(self::$uriAllProp);

        if ($res->getStatusCode() == 200) {

            return json_decode($res->getBody());
        } 
       
        return null;
    }

    public static function getPropietaireById($id) {
        
        $client = new Client();
        $res = $client->get(self::$uriPropById.$id);

        if ($res->getStatusCode() == 200) {

            return json_decode($res->getBody());
        } 
       
        return null;
     
    }
}