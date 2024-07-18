<?php
require_once 'database.php';

class Pelanggan
{
    private $db;
    private $table = 'pelanggan';
    public $id = "";
    public $kode = "";
    public $nama = "";
    public $jk = "";
    public $alamat = "";
    public $telepon = "";

    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }

    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }

    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function get_by_kode(int $kode)
    {
        $query = "SELECT * FROM $this->table WHERE kode = $kode";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode`, `nama`, `jk`, `alamat`, `telepon`) VALUES ('$this->kode', '$this->nama', '$this->jk', '$this->alamat', '$this->telepon')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kode` = '$this->kode', `nama` = '$this->nama', `jk` = '$this->jk', `alamat` = '$this->alamat', `telepon` = '$this->telepon' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kode($kode): int
    {
        $query = "UPDATE $this->table SET `nama` = '$this->nama', `jk` = '$this->jk', `alamat` = '$this->alamat', `telepon` = '$this->telepon' WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kode($kode): int
    {
        $query = "DELETE FROM $this->table WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
