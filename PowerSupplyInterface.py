from PowerSupplies import BKPRECISION9173

if __name__ == "__main__":
    bkp = BKPRECISION9173()
    bkp.set_voltage(1, 6)
    bkp.set_voltage(2, 6)
    bkp.set_current(1, 1.5)
    bkp.set_current(2, 1.5)
    # bkp.turn_channel_on(2)
    # time.sleep(2)
    # bkp.turn_channel_off(2)
    bkp.close()
