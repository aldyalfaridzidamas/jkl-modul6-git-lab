#!/usr/bin/env python3
"""Otomatisasi pembuatan VLAN pada switch akses."""

VLAN_DB = {}


def add_vlan(vlan_id, name):
    """Menambahkan VLAN jika belum terdaftar."""
    if vlan_id in VLAN_DB:
        print("VLAN " + str(vlan_id) + " sudah ada, dilewati")
        return False
    VLAN_DB[vlan_id] = name
    print("VLAN " + str(vlan_id) + " (" + name + ") dibuat")
    return True


def main():
    daftar_vlan = [(10, "DATA"), (20, "VOICE"), (30, "SERVER")]
    for vlan_id, nama in daftar_vlan:
        add_vlan(vlan_id, nama)
    print("Total VLAN aktif: " + str(len(VLAN_DB)))


if __name__ == "__main__":
    main()
