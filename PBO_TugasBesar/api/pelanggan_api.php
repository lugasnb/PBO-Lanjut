<?php
require_once 'database.php';
require_once 'pelanggan.php';

$db = new MySQLDatabase();
$pelanggan = new Pelanggan($db);
$id = 0;
$kode = 0;

$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kode'])) {
            $kode = $_GET['kode'];
        }
        
        if ($id > 0) {    
            $result = $pelanggan->get_by_id($id);
        } elseif ($kode > 0) {
            $result = $pelanggan->get_by_kode($kode);
        } else {
            $result = $pelanggan->get_all();
        }
        
        $data = array();
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'POST':
        $pelanggan->kode = $_POST['kode'];
        $pelanggan->nama = $_POST['nama'];
        $pelanggan->jk = $_POST['jk'];
        $pelanggan->alamat = $_POST['alamat'];
        $pelanggan->telepon = $_POST['telepon'];
        $pelanggan->insert();
        
        $a = $db->affected_rows();

        if ($a > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Pelanggan data created successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Pelanggan data not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        $_PUT = [];
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kode'])) {
            $kode = $_GET['kode'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pelanggan->kode = $_PUT['kode'];
        $pelanggan->nama = $_PUT['nama'];
        $pelanggan->jk = $_PUT['jk'];
        $pelanggan->alamat = $_PUT['alamat'];
        $pelanggan->telepon = $_PUT['telepon'];
        if ($id > 0) {    
            $pelanggan->update($id);
        } elseif ($kode > 0) {
            $pelanggan->update_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if ($a > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Pelanggan data updated successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Pelanggan data update failed.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kode'])) {
            $kode = $_GET['kode'];
        }
        if ($id > 0) {    
            $pelanggan->delete($id);
        } elseif ($kode > 0) {
            $pelanggan->delete_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if ($a > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Pelanggan data deleted successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Pelanggan data delete failed.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}

$db->close();
?>
