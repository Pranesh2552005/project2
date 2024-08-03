from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.garden.mapview import MapView, MapMarker
from plyer import gps

class GoogleMapsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.mapview = MapView(zoom=15)
        layout.add_widget(self.mapview)
        gps.configure(on_location=self.update_map)
        gps.start()

        return layout

    def update_map(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        self.mapview.center_on(lat, lon)
        self.mapview.remove_marker("current_location")
        marker = MapMarker(lat=lat, lon=lon)
        self.mapview.add_marker(marker, "current_location")

if __name__ == '__main__':
    GoogleMapsApp().run()
