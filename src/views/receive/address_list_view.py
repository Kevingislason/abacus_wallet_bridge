from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from controllers.main_controller import MainController
from models.watch_only_wallet import WatchOnlyWallet
from views.modal_view import Message, Modal


class AddressListView(QFrame):
    controller: MainController
    watch_only_wallet: WatchOnlyWallet
    incoming_balance: int

    def __init__(self, controller: MainController, watch_only_wallet: WatchOnlyWallet):
      super().__init__()
      self.controller = controller
      self.watch_only_wallet = watch_only_wallet
      self.watch_only_wallet.incoming_balance_satoshis_changed.connect(
          self.handle_incoming_balance_changed
      )

      self.size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
      self.size_policy.setHorizontalStretch(2)
      self.setSizePolicy(self.size_policy)
      self.layout = QVBoxLayout()
      self.setLayout(self.layout)

      self.modal = Modal()

      self.scroll = QScrollArea()
      self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
      self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
      self.scroll.setWidgetResizable(True)
      self.scroll.setAlignment(Qt.Alignment.AlignTop)
      self.list = QListWidget()
      self.scroll.setWidget(self.list)

      for address in self.watch_only_wallet.ui_addresses:
          address_widget = QListWidgetItem(address.label)
          icon_style = QStyle.StandardPixmap.SP_DialogYesButton if address.is_fresh else QStyle.StandardPixmap.SP_DialogNoButton
          icon = self.style().standardIcon(icon_style)
          address_widget.setIcon(icon)
          self.list.addItem(address_widget)

      self.new_address_name_input = QLineEdit()
      self.new_address_name_input.setMaxLength(32)
      self.new_address_name_input.setPlaceholderText("Label (Required)")
      self.new_address_name_input.setAlignment(Qt.Alignment.AlignBottom)

      self.new_address_button = QPushButton("Generate New Receiving Address")
      self.new_address_button.clicked.connect(self.handle_new_address_button_clicked)

      self.layout.addWidget(self.scroll)
      self.layout.addWidget(self.new_address_name_input)
      self.layout.addWidget(self.new_address_button)


    def handle_new_address_button_clicked(self):
        if self.watch_only_wallet.has_reached_gap_limit:
            self.modal.show(Message.GAP_LIMIT_REACHED)
            return

        address_label = self.new_address_name_input.text()
        if not address_label:
            return

        self.new_address_name_input.clear()
        new_address = self.controller.derive_external_address(address_label)
        address_widget = QListWidgetItem(address_label)
        icon_style = QStyle.StandardPixmap.SP_DialogYesButton
        icon = self.style().standardIcon(icon_style)
        address_widget.setIcon(icon)
        self.list.clearSelection()
        self.list.insertItem(0, address_widget)
        self.list.setCurrentRow(0)
        self.list.setFocus()

    @pyqtSlot(int)
    def handle_incoming_balance_changed(self, incoming_balance: int):
        for i, address in enumerate(self.watch_only_wallet.ui_addresses):
            if not address.is_fresh:
                list_item = self.list.item(i)
                icon_style = QStyle.SP_DialogNoButton
                icon = self.style().standardIcon(icon_style)
                list_item.setIcon(icon)


