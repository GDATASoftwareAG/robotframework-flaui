using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Collections.Generic;
using System;

namespace WpfApplication
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow
    {
        private List<Key> _keysUp = new List<Key>();
        private List<Key> _keysDown = new List<Key>();
        private DateTime DownTime;
        private DateTime UpTime;

        public MainWindow()
        {
            InitializeComponent();
            var vm = new MainViewModel();
            DataContext = vm;
        }

        private void Selector_OnSelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            foreach (var item in e.AddedItems)
            {
                var textBlock = (TextBlock) item;
                if (textBlock.Text == "Item 4")
                {
                    MessageBox.Show("Do you really want to do it?");
                }
            }
        }
        
        private void OnShowLabel(object sender, RoutedEventArgs e)
        {
            MenuItem menuitem = sender as MenuItem;
            if (menuitem == null) { return; }
            
            if (menuitem.IsChecked == true)
            {
                lblMenuChk.Visibility = Visibility.Visible;
            }
            else
            {
                lblMenuChk.Visibility = Visibility.Hidden;
            }
        }

        private void OnKeyDown(object sender, KeyEventArgs e)
        {
            AddKey(_keysDown, e.Key);
            lblKeyboardKeyDown.Content = GenerateKeyboardOutput(_keysDown);
        }

        private void OnKeyUp(object sender, KeyEventArgs e)
        {
            AddKey(_keysUp, e.Key);
            lblKeyboardKeyUp.Content = GenerateKeyboardOutput(_keysUp);
            RemoveKey(e.Key);
        }

        private static void AddKey(ICollection<Key> keys, Key key)
        {
            if (!keys.Contains(key))
            {
                keys.Add(key);
            }
        }

        private void RemoveKey(Key key)
        {
            _keysDown.Remove(key);
            if (_keysDown.Count == 0)
            {
                _keysUp.Clear();
            }
        }

        private static string GenerateKeyboardOutput(IReadOnlyList<Key> keys)
        {
            var output = "";

            for (var i = 0; i < keys.Count; i++)
            {
                if (i == keys.Count - 1)
                {
                    output += keys[i];
                }
                else
                {
                    output += keys[i] + "+";
                }
            }

            return output;
        }

        private void ResetKeyboard_Click(object sender, RoutedEventArgs e)
        {
            _keysDown.Clear();
            _keysUp.Clear();
            lblKeyboardKeyDown.Content = GenerateKeyboardOutput(_keysDown);
            lblKeyboardKeyUp.Content = GenerateKeyboardOutput(_keysUp);
        }

        private void ClickAndHoldButton_MouseDown(object sender, MouseButtonEventArgs e)
        {
            DownTime = DateTime.Now;
        }

        private void ClickAndHoldButton_MouseUp(object sender, MouseButtonEventArgs e)
        {
            UpTime = DateTime.Now;
            TimeSpan differene = UpTime - DownTime;
            ClickAndHoldButton.Content = differene.TotalSeconds.ToString();
        }

        private void ClickAndHoldButton_PreviewMouseDown(object sender, MouseButtonEventArgs e)
        {
            ClickAndHoldButton_MouseDown(sender,e);
        }

        private void ClickAndHoldButton_PreviewMouseUp(object sender, MouseButtonEventArgs e)
        {
            ClickAndHoldButton_MouseUp(sender, e);
        }

        private void ClickAndHoldButton_PreviewMouseRightButtonUp(object sender, MouseButtonEventArgs e)
        {
            ClickAndHoldButton_MouseUp(sender, e);
        }

        private void ClickAndHoldButton_PreviewMouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            ClickAndHoldButton_MouseDown(sender, e);
        }

    }
}
