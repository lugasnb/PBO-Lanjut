<?php
include 'database.php';

header("Content-Type: application/json");

$request_method = $_SERVER["REQUEST_METHOD"];
switch ($request_method) {
    case 'GET':
        if (!empty($_GET["id"])) {
            $id = intval($_GET["id"]);
            get_customer($id);
        } else {
            get_customer();
        }
        break;
    case 'POST':
        insert_customer();
        break;
    case 'PUT':
        $id = intval($_GET["id"]);
        update_customer($id);
        break;
    case 'DELETE':
        $id = intval($_GET["id"]);
        delete_customer($id);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}

function get_customer($id = 0)
{
    global $conn;
    $query = "SELECT * FROM customer";
    if ($id != 0) {
        $query .= " WHERE id_customer=" . $id . " LIMIT 1";
    }
    $response = array();
    $stmt = $conn->prepare($query);
    $stmt->execute();
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $response[] = $row;
    }
    echo json_encode($response);
}

function insert_customer()
{
    global $conn;
    $data = json_decode(file_get_contents('php://input'), true);
    $ktp = $data["ktp"];
    $nama_customer = $data["nama_customer"];
    $jk = $data["jk"];
    $kota = $data["kota"];
    $query = "INSERT INTO customer (ktp, nama_customer, jk, kota) VALUES ('$ktp', '$nama_customer', '$jk', '$kota')";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Customer added successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Customer addition failed.');
    }
    echo json_encode($response);
}

function update_customer($id)
{
    global $conn;
    $data = json_decode(file_get_contents("php://input"), true);
    $ktp = $data["ktp"];
    $nama_customer = $data["nama_customer"];
    $jk = $data["jk"];
    $kota = $data["kota"];
    $query = "UPDATE customer SET ktp='$ktp', nama_customer='$nama_customer', jk='$jk', kota='$kota' WHERE id_customer='$id'";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Customer updated successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Customer update failed.');
    }
    echo json_encode($response);
}

function delete_customer($id)
{
    global $conn;
    $query = "DELETE FROM customer WHERE id_customer='$id'";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Customer deleted successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Customer deletion failed.');
    }
    echo json_encode($response);
}
?>
