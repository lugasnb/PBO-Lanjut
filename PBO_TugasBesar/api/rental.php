<?php
require_once 'database.php';

class Rental
{
    private $db;
    private $table = 'rental';
    public $kodeps = "";
    public $kdpelanggan = "";
    public $tipe_ps = "";
    public $mulai = "";
    public $selesai = "";

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

    public function get_by_kodeps(string $kodeps)
    {
        $query = "SELECT * FROM $this->table WHERE kodeps = '$kodeps'";
        $result_set = $this->db->query($query);
        return $result_set;
    }

    public function get_pelanggan()
    {
        $query = "SELECT * FROM pelanggan";
        $result_set = $this->db->query($query);
        $pelanggan = [];
        while ($row = $this->db->fetch_assoc($result_set)) {
            $pelanggan[] = $row;
        }
        return $pelanggan;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeps`, `kdpelanggan`, `tipe_ps`, `mulai`, `selesai`) 
                  VALUES ('$this->kodeps', '$this->kdpelanggan', '$this->tipe_ps', '$this->mulai', '$this->selesai')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kodeps` = '$this->kodeps', `kdpelanggan` = '$this->kdpelanggan', 
                  `tipe_ps` = '$this->tipe_ps', `mulai` = '$this->mulai', `selesai` = '$this->selesai' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kodeps(string $kodeps): int
    {
        $query = "UPDATE $this->table SET `kdpelanggan` = '$this->kdpelanggan', `tipe_ps` = '$this->tipe_ps', 
                  `mulai` = '$this->mulai', `selesai` = '$this->selesai' WHERE kodeps = '$kodeps'";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kodeps(string $kodeps): int
    {
        $query = "DELETE FROM $this->table WHERE kodeps = '$kodeps'";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
