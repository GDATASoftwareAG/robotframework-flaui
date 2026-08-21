using System.Collections.ObjectModel;
using System.Windows.Input;
using WpfApplication.Infrastructure;

namespace WpfApplication
{
    public class MainViewModel : ObservableObject
    {
        public ObservableCollection<DataGridItem> DataGridItems { get; }

        public ObservableCollection<DataGridItem> LargeDataGridItems { get; }

        public MainViewModel()
        {
            DataGridItems = new ObservableCollection<DataGridItem>
            {
                new DataGridItem { Name = "John", Number = 12, IsChecked = false },
                new DataGridItem { Name = "Doe", Number = 24, IsChecked = true },
            };

            LargeDataGridItems = new ObservableCollection<DataGridItem>();
            for (int i = 0; i < 80; i++)
            {
                LargeDataGridItems.Add(new DataGridItem
                {
                    Name = $"Row {i:00}",
                    Number = i,
                    IsChecked = i % 2 == 0
                });
            }
        }
    }
}
