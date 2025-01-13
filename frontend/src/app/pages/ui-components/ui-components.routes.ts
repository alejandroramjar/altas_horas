import { Routes } from '@angular/router';
/*
En este archivo se define con la siguiente configuracion, cuando se agreag un componente para que este se muestre debe
 listarse cmo ruta siendo el path la ruta fisica en carpeta y componenet el nombre del componente a renderizar en ese
 momento, esto garantixza que este sea selecionado

 */
// ui
import { AppBadgeComponent } from './badge/badge.component';
import { AppChipsComponent } from './chips/chips.component';
import { AppListsComponent } from './lists/lists.component';
import { AppMenuComponent } from './menu/menu.component';
import { AppTooltipsComponent } from './tooltips/tooltips.component';
import { AppFormsComponent } from './forms/forms.component';
import { AppTablesComponent } from './tables/tables.component';
import { AppProductsTablesComponent} from "./products/products.component";
import {AppRegitroProductComponent} from "./registrar_producto/registro_product.component";

export const UiComponentsRoutes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'badge',
        component: AppBadgeComponent,
      },
      {
        path: 'chips',
        component: AppChipsComponent,
      },
      {
        path: 'lists',
        component: AppListsComponent,
      },
      {
        path: 'menu',
        component: AppMenuComponent,
      },
      {
        path: 'tooltips',
        component: AppTooltipsComponent,
      },
      {
        path: 'forms',
        component: AppFormsComponent,
      },
      {
        path: 'registrar_producto',
        component: AppRegitroProductComponent,
      },
      {
        path: 'tables',
        component: AppTablesComponent,
      },
      {
        path: 'products',
        component: AppProductsTablesComponent,
      },
    ],
  },
];
