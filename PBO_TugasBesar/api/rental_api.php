<?php
require_once 'database.php';
require_once 'rental.php';

$db = new MySQLDatabase();
$rental = new Rental($db);
$id = 0;
$kodeps = '';

// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kodeps'])) {
            $kodeps = $_GET['kodeps'];
        }
        
        if ($id > 0) {    
            $result = $rental->get_by_id($id);
        } elseif (!empty($kodeps)) {
            $result = $rental->get_by_kodeps($kodeps);
        } else {
            $result = $rental->get_all();
        }        

        // Check if result is from rental table or pelanggan table
        $items = [];
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $items[] = $row;
            }
        } else {
            // If no result from rental table, fetch pelanggan data
            $items = $rental->get_pelanggan();
        }

        header('Content-Type: application/json');
        echo json_encode($items);
        break;

    case 'POST':
        // Add a new rental
        $requestData = json_decode(file_get_contents('php://input'), true);
        $rental->kodeps = $requestData['kodeps'];
        $rental->kdpelanggan = $requestData['kdpelanggan'];
        $rental->tipe_ps = $requestData['tipe_ps'];
        $rental->mulai = $requestData['mulai'];
        $rental->selesai = $requestData['selesai'];
        $rentalId = $rental->insert();
        
        if ($rentalId > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Rental data created successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Rental data not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing rental
        $requestData = json_decode(file_get_contents('php://input'), true);
        
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kodeps'])) {
            $kodeps = $_GET['kodeps'];
        }
        
        $rental->kodeps = $requestData['kodeps'];
        $rental->kdpelanggan = $requestData['kdpelanggan'];
        $rental->tipe_ps = $requestData['tipe_ps'];
        $rental->mulai = $requestData['mulai'];
        $rental->selesai = $requestData['selesai'];
        
        if ($id > 0) {    
            $rental->update($id);
        } elseif (!empty($kodeps)) {
            $rental->update_by_kodeps($kodeps);
        } 
        
        $affectedRows = $db->affected_rows();

        if ($affectedRows > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Rental data updated successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Rental data update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a rental
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
        }
        if (isset($_GET['kodeps'])) {
            $kodeps = $_GET['kodeps'];
        }
        
        if ($id > 0) {    
            $rental->delete($id);
        } elseif (!empty($kodeps)) {
            $rental->delete_by_kodeps($kodeps);
        } 
        
        $affectedRows = $db->affected_rows();

        if ($affectedRows > 0) {
            $data['status'] = 'success';
            $data['message'] = 'Rental data deleted successfully.';
        } else {
            $data['status'] = 'failed';
            $data['message'] = 'Rental data delete failed.';
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
