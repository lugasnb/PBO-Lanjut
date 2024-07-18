<?php
include 'database.php';

header("Content-Type: application/json");

$request_method = $_SERVER["REQUEST_METHOD"];
switch ($request_method) {
    case 'GET':
        if (!empty($_GET["id"])) {
            $id = intval($_GET["id"]);
            get_barang($id);
        } else {
            get_barang();
        }
        break;
    case 'POST':
        insert_barang();
        break;
    case 'PUT':
        $id = intval($_GET["id"]);
        update_barang($id);
        break;
    case 'DELETE':
        $id = intval($_GET["id"]);
        delete_barang($id);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}

function get_barang($id = 0)
{
    global $conn;
    $query = "SELECT * FROM barang";
    if ($id != 0) {
        $query .= " WHERE id_barang=" . $id . " LIMIT 1";
    }
    $response = array();
    $stmt = $conn->prepare($query);
    $stmt->execute();
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $response[] = $row;
    }
    echo json_encode($response);
}

function insert_barang()
{
    global $conn;
    $data = json_decode(file_get_contents('php://input'), true);
    $kode_barang = $data["kode_barang"];
    $nama_barang = $data["nama_barang"];
    $harga = $data["harga"];
    $query = "INSERT INTO barang (kode_barang, nama_barang, harga) VALUES ('$kode_barang', '$nama_barang', '$harga')";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Barang added successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Barang addition failed.');
    }
    echo json_encode($response);
}

function update_barang($id)
{
    global $conn;
    $data = json_decode(file_get_contents("php://input"), true);
    $kode_barang = $data["kode_barang"];
    $nama_barang = $data["nama_barang"];
    $harga = $data["harga"];
    $query = "UPDATE barang SET kode_barang='$kode_barang', nama_barang='$nama_barang', harga='$harga' WHERE id_barang='$id'";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Barang updated successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Barang update failed.');
    }
    echo json_encode($response);
}

function delete_barang($id)
{
    global $conn;
    $query = "DELETE FROM barang WHERE id_barang='$id'";
    if ($conn->exec($query)) {
        $response = array('status' => 1, 'status_message' => 'Barang deleted successfully.');
    } else {
        $response = array('status' => 0, 'status_message' => 'Barang deletion failed.');
    }
    echo json_encode($response);
}
?>
