<?php
require_once('login.php');

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    if (isset($data['username']) && isset($data['password'])) {
        $username = $data['username'];
        $password = $data['password'];

        $user = cekLogin($username, $password);

        if ($user) {
            $response = array('status' => 'success', 'message' => 'Login berhasil', 'user' => $user);
        } else {
            $response = array('status' => 'error', 'message' => 'Username atau password salah');
        }
    } else {
        $response = array('status' => 'error', 'message' => 'Data tidak lengkap');
    }
} else {
    $response = array('status' => 'error', 'message' => 'Metode HTTP tidak diizinkan');
}

echo json_encode($response);
?>
